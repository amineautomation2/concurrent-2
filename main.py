import argparse
import time

from ajbell import ajbell_runner
from ajbell.url import get_ajbell_url
from utils import create_spreadsheet, delay, get_xlsx_filepath
from worker import (
    merge_csv_to_xlsx,
)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", type=str, help="id worker")
    parser.add_argument("--max", type=str, help="max worker")
    parser.add_argument("--sheet", type=str, help="sheet name")
    parser.add_argument("--url", action="store_true", help="sheet name")
    parser.add_argument("--fresh", action="store_true", help="new spreadsheet")

    args = parser.parse_args()
    xlsx_out = get_xlsx_filepath("ajbell.xlsx")

    if args.fresh:
        create_spreadsheet(
            xlsx_out, ["Investment", "ETF", "MF"], ["Name", "ISIN", "URL", "Keyword"]
        )

    if args.url:
        sheet = args.url
        for sheet in ["Investment", "ETF", "MF"]:
            get_ajbell_url(sheet)
            delay(10, 20)
        return

    elif args.id and args.max and args.sheet:
        ajbell_runner(
            id_worker=int(args.id), max_workers=int(args.max), sheet=args.sheet
        )
        return

    elif args.sheet:
        merge_csv_to_xlsx(xlsx_out, ["name", "isin", "url", "keyword"], args.sheet)
        return


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    elapsed = time.perf_counter() - start
    print(f"Execution time: {elapsed:.2f} seconds.")
