import os

import matplotlib.pyplot as plt


def plot_weekly(table, city, save=False):
    target_city = table[table['city'] == city]["temperature"].reset_index(drop=True)

    target_city.plot(kind="line", color="skyblue")
    plt.title(f"{city}: почасовая температура за неделю")
    plt.ylabel("Температура в °C")
    plt.xlabel("Часы")
    plt.tight_layout()

    if save:
        os.makedirs("pictures", exist_ok=True)
        filename = f"pictures/weekly_{city}.png"
        plt.savefig(filename, bbox_inches="tight")
        print(f"График сохранён: {filename}")
    else:
        plt.show()