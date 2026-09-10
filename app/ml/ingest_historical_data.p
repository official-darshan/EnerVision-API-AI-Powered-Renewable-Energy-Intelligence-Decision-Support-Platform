import sys
import csv
from datetime import date, timedelta
import httpx

NASA_POWER_URL = "https://power.larc.nasa.gov/api/temporal/daily/point"

# Parameters: solar radiation, max/min temp, cloud-related humidity, wind speed
PARAMETERS = "ALLSKY_SFC_SW_DWN,T2M_MAX,T2M_MIN,RH2M,WS10M"


def fetch_historical_data(latitude: float, longitude: float, start: str, end: str) -> dict:
    params = {
        "parameters": PARAMETERS,
        "community": "RE",  # Renewable Energy community — correct parameter set for solar
        "longitude": longitude,
        "latitude": latitude,
        "start": start,
        "end": end,
        "format": "JSON",
    }

    response = httpx.get(NASA_POWER_URL, params=params, timeout=30.0)
    response.raise_for_status()
    return response.json()


def save_to_csv(data: dict, output_path: str):
    parameter_data = data["properties"]["parameter"]
    dates = sorted(parameter_data["ALLSKY_SFC_SW_DWN"].keys())

    with open(output_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "solar_radiation", "temp_max", "temp_min", "humidity", "windspeed"])

        for d in dates:
            writer.writerow([
                d,
                parameter_data["ALLSKY_SFC_SW_DWN"][d],
                parameter_data["T2M_MAX"][d],
                parameter_data["T2M_MIN"][d],
                parameter_data["RH2M"][d],
                parameter_data["WS10M"][d],
            ])

    print(f"Saved {len(dates)} days of data to {output_path}")


if __name__ == "__main__":
    latitude = float(sys.argv[1]) if len(sys.argv) > 1 else 19.0760
    longitude = float(sys.argv[2]) if len(sys.argv) > 2 else 72.8777

    end_date = date.today() - timedelta(days=3)  # NASA POWER has a short processing lag
    start_date = end_date - timedelta(days=365 * 2)  # 2 years of history

    print(f"Fetching NASA POWER data for ({latitude}, {longitude}) "
          f"from {start_date} to {end_date}...")

    data = fetch_historical_data(
        latitude, longitude,
        start_date.strftime("%Y%m%d"),
        end_date.strftime("%Y%m%d"),
    )

    save_to_csv(data, "data/historical_solar_mumbai.csv")