import argparse
import csv
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Inspect a CSV file and print a basic summary."
    )
    parser.add_argument("csv_path", help="Path to the CSV file to inspect")
    args = parser.parse_args()

    csv_path = Path(args.csv_path)

    if not csv_path.is_file():
        parser.error(f"File not found: {csv_path}")

    with csv_path.open(encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        column_names = next(reader)
        rows = list(reader)

    print(f"Rows: {len(rows)}")
    print(f"Columns: {len(column_names)}")
    print(f"Column names: {', '.join(column_names)}")


if __name__ == "__main__":
    main()