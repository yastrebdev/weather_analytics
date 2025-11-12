import os

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


def plot_influence(table, save=False):
    df = table.dropna(subset=["apparent_temperature", "humidity", "wind_speed", "precipitation"])

    X = df[["humidity", "wind_speed", "precipitation"]]
    y = df["apparent_temperature"]

    scaler_X = StandardScaler()
    scaler_y = StandardScaler()

    X_scaled = scaler_X.fit_transform(X)
    y_scaled = scaler_y.fit_transform(y.values.reshape(-1, 1)).ravel()

    model = LinearRegression().fit(X_scaled, y_scaled)

    coefs = pd.Series(model.coef_, index=X.columns)
    influence = (abs(coefs) / abs(coefs).sum() * 100).round(2)

    print("\nКоэффициенты влияния факторов:")
    print(coefs)

    print("\nВклад факторов в ощущаемую температуру (%):")
    print(influence)

    plt.figure(figsize=(6, 4))
    influence.plot(kind="bar", color="skyblue")
    plt.title("Влияние факторов на ощущаемую температуру")
    plt.ylabel("Вклад, %")
    plt.xlabel("Фактор")
    plt.tight_layout()

    if save:
        os.makedirs("pictures", exist_ok=True)
        plt.savefig("pictures/influence_factors.png", bbox_inches="tight")
        print("График сохранён: pictures/influence_factors.png")
    else:
        plt.show()