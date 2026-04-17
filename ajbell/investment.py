def get_investment_config() -> dict:
    cookies = {
        'cookiesession1': '678A3EB87F11D1A7753409816F1F7F0C',
        'TRD_SESSID': 'ct9drtv2farpeci9rcq56nt1naif2tc950d4qir5udfvtgo5',
        'cookie-agreed': 'C0000%2CC0002%2CC0003',
        'gid_ajb': 'c1b920b4-0ae2-3213-f090-faf0bec8c918',
    }

    headers = {
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:149.0) Gecko/20100101 Firefox/149.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9',
        # 'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Content-Type': 'application/json',
        'Authorization': 'YouInvestDeviceToken token=e26a3e21-06d0-5078-902b-35b08724hd18',
        'X-Trading-Brand': 'trading',
        'sentry-trace': 'f9f49463e680427d86a3f9b444e163c7-a6474b2bbc445953-0',
        'baggage': 'sentry-environment=production,sentry-public_key=b4279c8feba04f64ad81673adba2c031,sentry-trace_id=f9f49463e680427d86a3f9b444e163c7,sentry-org_id=532596,sentry-transaction=%2Fscreener%2Ftrusts,sentry-sampled=false,sentry-sample_rand=0.7805111774218437,sentry-sample_rate=0.1',
        'Origin': 'https://www.ajbell.co.uk',
        'Sec-GPC': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://www.ajbell.co.uk/market-research/screener/trusts',
        # 'Cookie': 'cookiesession1=678A3EB87F11D1A7753409816F1F7F0C; TRD_SESSID=ct9drtv2farpeci9rcq56nt1naif2tc950d4qir5udfvtgo5; cookie-agreed=C0000%2CC0002%2CC0003; gid_ajb=c1b920b4-0ae2-3213-f090-faf0bec8c918',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
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
        'screenerType': 'CEF',
        'rowsPerPage': 25,
    }

    return dict(cookies=cookies, headers=headers, payload=payload)


def get_investment_keyword() -> list[dict]:
    return []
