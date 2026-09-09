import sys
import pandas as pd

MISSING_VALUE_SENTINEL = -999


def load_raw_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, dtype={"date": str})
    df["date"] = pd.to_datetime(df["date"], format="%Y%m%d")
    return df


def report_missing_values(df: pd.DataFrame) -> None:
    numeric_cols = ["solar_radiation", "temp_max", "temp_min", "humidity", "windspeed"]
    for col in numeric_cols:
        missing_count = (df[col] == MISSING_VALUE_SENTINEL).sum()
        if missing_count > 0:
            print(f"  {col}: {missing_count} missing value(s) found (sentinel -999)")


def clean_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    numeric_cols = ["solar_radiation", "temp_max", "temp_min", "humidity", "windspeed"]
    df = df.copy()

    for col in numeric_cols:
        df.loc[df[col] == MISSING_VALUE_SENTINEL, col] = pd.NA

    before = len(df)
    df = df.dropna(subset=numeric_cols)
    after = len(df)

    if before != after:
        print(f"  Dropped {before - after} row(s) with missing values")

    return df


def add_time_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["day_of_year"] = df["date"].dt.dayofyear
    df["month"] = df["date"].dt.month
    return df


def validate_ranges(df: pd.DataFrame) -> None:
    # Sanity checks — these are physically reasonable bounds, not arbitrary
    checks = {
        "solar_radiation": (0, 12),      # kWh/m^2/day — realistic global range
        "temp_max": (-50, 55),           # Celsius
        "temp_min": (-60, 45),
        "humidity": (0, 100),            # percent
        "windspeed": (0, 50),            # m/s
    }
    for col, (low, high) in checks.items():
        out_of_range = df[(df[col] < low) | (df[col] > high)]
        if len(out_of_range) > 0:
            print(f"  WARNING: {len(out_of_range)} row(s) in '{col}' fall outside expected range [{low}, {high}]")


if __name__ == "__main__":
    input_path = sys.argv[1] if len(sys.argv) > 1 else "data/historical_solar_mumbai.csv"
    output_path = sys.argv[2] if len(sys.argv) > 2 else "data/historical_solar_mumbai_clean.csv"

    print(f"Loading raw data from {input_path}...")
    df = load_raw_data(input_path)
    print(f"Loaded {len(df)} rows")

    print("Checking for missing values (sentinel -999)...")
    report_missing_values(df)

    print("Cleaning missing values...")
    df = clean_missing_values(df)

    print("Adding time-based features...")
    df = add_time_features(df)

    print("Validating value ranges...")
    validate_ranges(df)

    df.to_csv(output_path, index=False)
    print(f"Saved {len(df)} clean rows to {output_path}")