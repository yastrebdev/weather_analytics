import os

import matplotlib.pyplot as plt


def plot_amplitude(table, x, y, save=False):
    data = table[[x, y]].copy()

    fig, ax = plt.subplots(figsize=(12, 6))

    bars = ax.bar(range(len(data)), data[y], color="skyblue")

    ax.set_title("Амплитуда температуры по городам")
    ax.set_ylabel("Амплитуда в °C")
    ax.set_xlabel("Индекс города")

    n = max(1, len(data) // 20)
    indices = range(0, len(data), n)
    ax.set_xticks(indices)
    ax.set_xticklabels(indices)

    annotation = ax.annotate("", xy=(0, 0), xytext=(20, 20), textcoords="offset points",
                             bbox=dict(boxstyle="round", fc="w", alpha=0.9),
                             arrowprops=dict(arrowstyle="->"))
    annotation.set_visible(False)

    def update_annotation(ind):
        idx = ind
        city = data.iloc[idx][x]
        amplitude = data.iloc[idx][y]
        annotation.xy = (idx, data.iloc[idx][y])
        annotation.set_text(f"Город: {city}\nАмплитуда: {amplitude}°C")
        annotation.set_visible(True)
        fig.canvas.draw_idle()

    def hover(event):
        if event.inaxes == ax:
            for bar in bars:
                cont, ind = bar.contains(event)
                if cont:
                    update_annotation(bars.index(bar))
                    return
            annotation.set_visible(False)
            fig.canvas.draw_idle()

    def on_click(event):
        if event.inaxes == ax:
            for bar in bars:
                cont, ind = bar.contains(event)
                if cont:
                    update_annotation(bars.index(bar))
                    return

    fig.canvas.mpl_connect("motion_notify_event", hover)
    fig.canvas.mpl_connect("button_press_event", on_click)

    plt.tight_layout()

    if save:
        os.makedirs("pictures", exist_ok=True)
        plt.savefig("pictures/amplitude_by_cities.png", bbox_inches="tight")
        print("График сохранён: pictures/amplitude_by_cities.png")
    else:
        plt.show()