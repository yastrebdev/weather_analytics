import json
import pandas as pd
from db.connection import get_connection
from db.models import save_cities, save_weather

def build_database():
    conn = get_connection()

    with open("./data/meteo_data.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    cities = []
    weather = []

    for city_name, info in data.items():
        cities.append({
            "city_id": len(cities) + 1,
            "city": city_name,
            "latitude": info["latitude"],
            "longitude": info["longitude"],
            "timezone": info["timezone"]
        })

        hourly = pd.DataFrame(info["hourly"])
        hourly["city_id"] = len(cities)
        weather.append(hourly)

    df_cities = pd.DataFrame(cities)
    df_weather = pd.concat(weather, ignore_index=True)

    save_cities(df_cities, conn)
    save_weather(df_weather, conn)

    print("Database successfully built.")

if __name__ == "__main__":
    build_database()