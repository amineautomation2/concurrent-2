def get_etf_config() -> dict:
    cookies = {
        'cookiesession1': '678A3EB87F11D1A7753409816F1F7F0C',
        'cookie-agreed': 'C0000%2CC0002%2CC0003',
        'gid_ajb': 'c1b920b4-0ae2-3213-f090-faf0bec8c918',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Content-Type': 'application/json',
        'Authorization': 'YouInvestDeviceToken token=e26a3e21-06d0-5078-902b-35b08724hd18',
        'X-Trading-Brand': 'trading',
        'sentry-trace': 'ac00c571ce2547029a5e507ba558d402-96359803d4294f76-0',
        'baggage': 'sentry-environment=production,sentry-public_key=b4279c8feba04f64ad81673adba2c031,sentry-trace_id=ac00c571ce2547029a5e507ba558d402,sentry-org_id=532596,sentry-transaction=%2Fscreener%2Fetf,sentry-sampled=false,sentry-sample_rand=0.15262426016756891,sentry-sample_rate=0.1',
        'Origin': 'https://www.ajbell.co.uk',
        'Sec-GPC': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://www.ajbell.co.uk/market-research/screener/etf',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
    }

    payload = {
        'SectorId': [],
        'IMASectorId': [],
        'LargestSector': [],
        'AdministratorCompanyId': [],
        'GlobalAssetClassId': [],
        'FundTNAV': [],
        'Yield_M12': [],
        'DividendYield': [],
        'Largestregion': [],
        'SRRI': [],
        'StarRating': [],
        'SustainabilityRating': [],
        'LatestReportOngoingCharge': [],
        'ReturnM12': [],
        'ReturnM36': [],
        'ReturnM60': [],
        'Distribution': [],
        'IndexFund': [],
        'FundsSelection': [],
        'IndexingApproach': [],
        'IndustryId': [],
        'PERatio': [],
        'MarketCap': [],
        'ExchangeId': [],
        'RegionExchangeId': [],
        'currentPage': 1,
        'selectedFunds': [],
        'search': '',
        'sortOrder': None,
        'screenerType': 'ETF',
        'rowsPerPage': 25,
    }

    return dict(cookies=cookies, headers=headers, payload=payload)


def get_etf_keyword() -> list[dict]:
    return []
