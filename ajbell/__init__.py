from worker import get_data_by_worker_id, get_xlsx_data, write_csv_by_id
from .keyword import get_ajbell_keyword
from utils import get_xlsx_filepath, setup_driver


def ajbell_runner(id_worker: int, max_workers: int, sheet: str) -> None:
    xlsx = get_xlsx_filepath("ajbell.xlsx")
    data = get_xlsx_data(xlsx, sheet)
    driver = setup_driver(True)
    fields = ["index", "name", "isin", "url", "keyword", "sheet"]
    funds_per_worker = get_data_by_worker_id(id_worker, max_workers, data)
    result = get_ajbell_keyword(driver, funds_per_worker)
    out_csv = f"ajbell_{id_worker}_{sheet.lower()}.csv"
    write_csv_by_id(out_csv, result, fields)
    driver.quit()
