import json
import requests
from datetime import date, timedelta
import time

today = date.today()
seven_days_ago_date = today - timedelta(days=7)

START_DATE=date.today()
END_DATE=seven_days_ago_date

url = "https://api.open-meteo.com/v1/forecast"

capitals = []

with open("data/capitals.csv", "r", encoding="utf-8") as file:
    for line in file.readlines()[1:]:
        capitals.append(line.strip().split(",")[1:])


def get_data_single_city(lat, lon, start_date, end_date, tz):
    response = requests.get(
        url=f"{url}?"
            f"latitude={lat}&"
            f"longitude={lon}&"
            f"start_date={start_date}&"
            f"end_date={end_date}&"
            f"hourly=temperature_2m,"
                f"relative_humidity_2m,"
                f"apparent_temperature,"
                f"wind_speed_10m,"
                f"precipitation&"
            f"timezone={tz}"
    )

    return response.json()


def get_multiple_data(cities):
    data = {}
    for i, city in enumerate(cities):
        name, lat, lon, tz = city
        try:
            data[name] = get_data_single_city(
                lat, lon, START_DATE, END_DATE, tz)
            time.sleep(0.5)
            print(f"Data received: {i + 1}/{len(cities)}")
        except Exception as e:
            print(f"Error for {name}: {e}")
    print(f"Completed!")
    return data


meteo_data = get_multiple_data(capitals)

with open("data/meteo_data.json", "w", encoding="utf-8") as f:
    json.dump(meteo_data, f, ensure_ascii=False, indent=2)