import math
import random
import time

from curl_cffi.requests import post
from utils import delay, get_xlsx_filepath, parse_ajbell_data, save_xlsx

from .etf import get_etf_config
from .investment import get_investment_config
from .mutual import get_mf_config


def get_ajbell_url(sheet: str) -> None:
    xlsx = get_xlsx_filepath("ajbell.xlsx")
    match sheet:
        case "Investment":
            config_it = get_investment_config()
            urls = get_funds_url(config_it)
            save_xlsx(
                xlsx_out=xlsx,
                funds=urls,
                cols=["name", "isin", "url"],
                sheet=sheet,
            )
        case "ETF":
            config_etf = get_etf_config()
            urls = get_funds_url(config_etf)
            save_xlsx(
                xlsx_out=xlsx,
                funds=urls,
                cols=["name", "isin", "url"],
                sheet=sheet,
            )
        case "MF":
            config_mf = get_mf_config()
            urls = get_funds_url(config_mf, is_mf=True)
            save_xlsx(
                xlsx_out=xlsx,
                funds=urls,
                cols=["name", "isin", "url"],
                sheet=sheet,
            )


def get_funds_url_old(config: dict, is_mf: bool = False) -> list[dict]:
    cookies = config["cookies"]
    headers = config["headers"]
    payload = config["payload"]
    funds_url = []
    response = post(
        "https://www.ajbell.co.uk/market-research/api/screener",
        cookies=cookies,
        headers=headers,
        json=payload,
        impersonate="chrome",
    )
    if response.status_code != 200:
        raise Exception("error: ", response.status_code)
    data = response.json()
    funds = parse_ajbell_data(data["rows"], is_mf)
    funds_url.extend(funds)

    total_pages = math.ceil(data["total"] / data["pageSize"])
    for page in range(2, total_pages + 1):
        payload.update({"currentPage": page})
        response = post(
            "https://www.ajbell.co.uk/market-research/api/screener",
            cookies=cookies,
            headers=headers,
            json=payload,
            impersonate="chrome",
        )
        data = response.json()
        data = parse_ajbell_data(data["rows"], is_mf)
        funds_url.extend(data)
        delay(1, 2)
    return funds_url


def get_funds_url(config: dict, is_mf: bool = False) -> list[dict]:
    payload = config["payload"].copy()
    cookies = config["cookies"]
    headers = config["headers"]
    funds_url = []

    # First request
    response = post(
        "https://www.ajbell.co.uk/market-research/api/screener",
        cookies=cookies,
        headers=headers,
        json=payload,
        impersonate="chrome",
    )

    if response.status_code != 200:
        raise Exception(
            f"Initial request failed with status code: {response.status_code}"
        )

    try:
        data = response.json()
    except Exception as e:
        raise Exception(
            f"Failed to parse JSON on initial request. Raw response: {response.text[:200]}"
        ) from e

    if not data.get("total") or not data.get("rows"):
        return funds_url

    funds = parse_ajbell_data(data["rows"], is_mf)
    funds_url.extend(funds)

    page_size = data.get("pageSize", 20)
    if page_size == 0:
        return funds_url

    total_pages = math.ceil(data["total"] / page_size)

    # Pagination loop
    for page in range(2, total_pages + 1):
        payload["currentPage"] = page

        max_retries = 3
        base_delay = 2  # starting delay in seconds
        page_success = False

        for attempt in range(max_retries + 1):
            try:
                response = post(
                    "https://www.ajbell.co.uk/market-research/api/screener",
                    cookies=cookies,
                    headers=headers,
                    json=payload,
                    impersonate="chrome",
                )

                if response.status_code != 200:
                    raise ValueError(f"Status code {response.status_code}")

                page_data = response.json()

                # Check if page is empty but valid (out of bounds edge case)
                if "rows" not in page_data or not page_data["rows"]:
                    print(f"Page {page} returned empty rows. Ending sequence.")
                    return (
                        funds_url  # Break entirely if the api run is cleanly finished
                    )

                parsed_data = parse_ajbell_data(page_data["rows"], is_mf)
                funds_url.extend(parsed_data)
                page_success = True
                break  # Success! Escape retry loop

            except (Exception, ValueError) as e:
                if attempt < max_retries:
                    # Exponential backoff: base * 2^attempt + full jitter
                    backoff = (base_delay * (2**attempt)) + random.uniform(0, 1)
                    print(
                        f"Error pulling page {page} ({e}). Retry {attempt + 1}/{max_retries} in {backoff:.2f}s..."
                    )
                    time.sleep(backoff)
                else:
                    print(f"Skipping page {page}: Failed after {max_retries} retries.")

        # Add normal rate limit spacing between pages only if the last attempt succeeded
        if page_success:
            delay(1, 2)

    return funds_url
