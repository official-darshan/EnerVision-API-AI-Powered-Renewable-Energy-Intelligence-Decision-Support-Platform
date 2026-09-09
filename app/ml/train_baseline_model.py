import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

FEATURES = ["humidity", "temp_max", "windspeed", "day_of_year"]
TARGET = "solar_radiation"


def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["date"])
    return df.sort_values("date").reset_index(drop=True)


def time_aware_split(df: pd.DataFrame, test_fraction: float = 0.2):
    split_index = int(len(df) * (1 - test_fraction))
    train_df = df.iloc[:split_index]
    test_df = df.iloc[split_index:]
    return train_df, test_df


def train_and_evaluate(train_df: pd.DataFrame, test_df: pd.DataFrame):
    X_train, y_train = train_df[FEATURES], train_df[TARGET]
    X_test, y_test = test_df[FEATURES], test_df[TARGET]

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    rmse = mean_squared_error(y_test, predictions) ** 0.5
    r2 = r2_score(y_test, predictions)

    print(f"Test set size: {len(test_df)} rows")
    print(f"MAE:  {mae:.4f} kWh/m²/day")
    print(f"RMSE: {rmse:.4f} kWh/m²/day")
    print(f"R²:   {r2:.4f}")

    return model, {"mae": mae, "rmse": rmse, "r2": r2}


if __name__ == "__main__":
    df = load_data("data/historical_solar_mumbai_clean.csv")
    print(f"Loaded {len(df)} rows, date range {df['date'].min().date()} to {df['date'].max().date()}")

    train_df, test_df = time_aware_split(df)
    print(f"Train: {len(train_df)} rows ({train_df['date'].min().date()} to {train_df['date'].max().date()})")
    print(f"Test:  {len(test_df)} rows ({test_df['date'].min().date()} to {test_df['date'].max().date()})")

    model, metrics = train_and_evaluate(train_df, test_df)

    joblib.dump(model, "models/baseline_linear_regression.pkl")
    print("Model saved to models/baseline_linear_regression.pkl")