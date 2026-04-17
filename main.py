import argparse
import time
from ajbell import ajbell_runner
from ajbell.url import get_ajbell_url
from utils import delay, get_xlsx_filepath
from worker import (
    merge_csv_to_xlsx,
)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", type=str, help="id worker")
    parser.add_argument("--sheet", type=str, help="sheet name")
    parser.add_argument("--url", type=str, help="sheet name")

    args = parser.parse_args()
    xlsx_out = get_xlsx_filepath("ajbell.xlsx")
    if args.url:
        sheet = args.url
        if args.url == "all":
            for sheet in ["Investment", "ETF", "MF"]:
                get_ajbell_url(sheet)
                delay(10, 20)
            return
        get_ajbell_url(sheet)

    elif args.id and args.sheet:
        # id_worker = int(sys.argv[1])
        start = time.perf_counter()
        ajbell_runner(id_worker=int(args.id),
                      max_workers=5, sheet=args.sheet)
        elapsed = time.perf_counter() - start
        print(f"Execution time: {elapsed:.2f} seconds.")
        return

    elif args.sheet:
        merge_csv_to_xlsx(
            xlsx_out, ["name", "isin", "url", "keyword"], args.sheet)
        return


if __name__ == "__main__":
    main()
