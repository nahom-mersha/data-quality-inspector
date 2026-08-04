import argparse
from pathlib import Path

import pandas as pd
import yaml


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

    missing_values = dataframe.isna().sum()

    print("\nMissing values:")

    for column_name, missing_count in missing_values.items():
        if missing_count > 0:
            missing_percentage = (missing_count / len(dataframe)) * 100
            print(
                f"- {column_name}: {missing_count} missing value "
                f"({missing_percentage:.1f}%)"
            )
    duplicate_count = dataframe.duplicated().sum()

    print(f"\nDuplicate rows: {duplicate_count}")

    unique_value_counts = dataframe.nunique()

    print("\nConstant columns:")

    for column_name, unique_count in unique_value_counts.items():
        if unique_count == 1:
            constant_value = dataframe[column_name].dropna().iloc[0]
            print(f"- {column_name}: {constant_value}")

    schema_path = Path("configs/schema.yaml")

    with schema_path.open(encoding="utf-8") as file:
        schema = yaml.safe_load(file)

    age_rules = schema["columns"]["age"]

    age_values = pd.to_numeric(dataframe["age"], errors="coerce")
    invalid_type_values = dataframe["age"].notna() & age_values.isna()

    below_minimum = age_values < age_rules["minimum"]
    above_maximum = age_values > age_rules["maximum"]
    invalid_type_count = invalid_type_values.sum()
    below_minimum_count = below_minimum.sum()
    above_maximum_count = above_maximum.sum()

    print("\nSuspicious values:")

    if invalid_type_count > 0:
        print(f"- age: {invalid_type_count} non-numeric value(s)")

    if below_minimum_count > 0:
        print(
            f"- age: {below_minimum_count} value(s) below "
            f"the allowed minimum of {age_rules['minimum']}"
        )

    if above_maximum_count > 0:
        print(
            f"- age: {above_maximum_count} value(s) above "
            f"the allowed maximum of {age_rules['maximum']}"
        )


if __name__ == "__main__":
    main()
