import pandas as pd


def temp_agg_data_by_city_query(conn, *, limit=None, order_by="avg_day_temp", order_dir="DESC"):
    query = """
        SELECT city
            , ROUND(AVG(temperature_2m), 2) AS avg_day_temp
            , MAX(temperature_2m) AS max_temp
            , MIN(temperature_2m) AS min_temp
            , MAX(temperature_2m) - MIN(temperature_2m) AS amplitude
        FROM cities
            JOIN weather USING(city_id)
        WHERE TIME(time) BETWEEN TIME("12:00") AND TIME("18:00")
        GROUP BY city
    """

    params = []

    order_dir = order_dir.upper()
    if order_dir not in ['ASC', 'DESC']:
        order_dir = 'DESC'

    allowed_columns = ['city', 'avg_day_temp']
    if order_by in allowed_columns:
        query += f" ORDER BY {order_by} {order_dir}"
    else:
        query += " ORDER BY avg_day_temp DESC"

    if limit is not None:
        query += " LIMIT ?"
        params.append(limit)

    return pd.read_sql(query, conn, params=params if params else None)