import pandas as pd


def save_cities(df_cities: pd.DataFrame, conn):
    df_cities.to_sql("cities", conn, index=False, if_exists="replace")


def save_weather(df_weather: pd.DataFrame, conn):
    df_weather.to_sql("weather", conn, index=False, if_exists="replace")