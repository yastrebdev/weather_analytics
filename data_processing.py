import pandas as pd
from db.connection import get_connection

def load_and_prepare_data():
    conn = get_connection()

    df_cities = pd.read_sql("SELECT * FROM cities", conn)
    df_weather = pd.read_sql("SELECT * FROM weather", conn)

    conn.close()

    df_weather = df_weather.rename(columns={
        "temperature_2m": "temperature",
        "relative_humidity_2m": "humidity",
        "wind_speed_10m": "wind_speed",
    })

    df_weather["time"] = pd.to_datetime(df_weather["time"])
    merged = pd.merge(df_cities, df_weather, on="city_id", how="inner")

    filtered = merged[
        (merged["time"].dt.hour >= 12) & (merged["time"].dt.hour <= 18)
    ]

    city_temp = filtered[["city", "temperature"]]

    agg = (
        city_temp.groupby("city", as_index=False)
        .agg(
            min_temp=("temperature", "min"),
            max_temp=("temperature", "max"),
            avg_temp=("temperature", "mean"),
            amplitude=("temperature", lambda x: x.max() - x.min())
        )
        .round(2)
    )

    return merged, agg