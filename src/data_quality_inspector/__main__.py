import argparse
from pathlib import Path

import pandas as pd


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Inspect a CSV file and print a basic summary."
    )
    parser.add_argument("csv_path", help="Path to the CSV file to inspect")
    args = parser.parse_args()

    csv_path = Path(args.csv_path)

    if not csv_path.is_file():
        parser.error(f"File not found: {csv_path}")

    dataframe = pd.read_csv(csv_path)

    print("Dataset loaded successfully")
    print()
    print(f"Rows: {len(dataframe)}")
    print(f"Columns: {len(dataframe.columns)}")
    print(f"Column names: {', '.join(dataframe.columns)}")


if __name__ == "__main__":
    main()
