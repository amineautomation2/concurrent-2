import math
from curl_cffi.requests import post
from .investment import get_investment_config
from .etf import get_etf_config
from .mutual import get_mf_config
from utils import delay, get_xlsx_filepath, save_xlsx, parse_ajbell_data


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


def get_funds_url(config: dict, is_mf: bool = False) -> list[dict]:
    cookies = config["cookies"]
    headers = config["headers"]
    payload = config["payload"]
    funds_url = []
    response = post('https://www.ajbell.co.uk/market-research/api/screener',
                    cookies=cookies, headers=headers, json=payload, impersonate='chrome')
    if response.status_code != 200:
        raise Exception("error: ", response.status_code)
    data = response.json()
    funds = parse_ajbell_data(data["rows"], is_mf)
    funds_url.extend(funds)

    total_pages = math.ceil(data["total"] / data["pageSize"])
    for page in range(2, total_pages+1):
        payload.update({'currentPage': page})
        response = post('https://www.ajbell.co.uk/market-research/api/screener',
                        cookies=cookies, headers=headers, json=payload, impersonate='chrome')
        data = response.json()
        data = parse_ajbell_data(data["rows"], is_mf)
        funds_url.extend(data)
        delay(1, 2)
    return funds_url
