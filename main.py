from cli import parse_args
from data_processing import load_and_prepare_data
from plotting.amplitude import plot_amplitude
from plotting.weekly import plot_weekly
from plotting.influence import plot_influence


def main():
    args = parse_args()
    merge_city_and_weather, temp_agg_data_by_city = load_and_prepare_data()

    if args.tables:
        print("\n=== Таблицы ===")
        print("1. Средняя дневная температура\n2. Дневной максимум и минимум\n3. Амплитуда (max-min)")
        print(temp_agg_data_by_city)

        city_max_amplitude = temp_agg_data_by_city.loc[
            temp_agg_data_by_city["amplitude"].idxmax(), ["city", "amplitude"]
        ]
        print("\nГород с наибольшим перепадом дневной температуры:")
        print(city_max_amplitude)

    elif args.amplitude:
        print("Построение графика амплитуды...")
        plot_amplitude(temp_agg_data_by_city, "city", "amplitude", save=args.save)

    elif args.weekly:
        if not args.city:
            print("Укажите город: --weekly --city Moscow")
            return
        print(f"Построение недельного графика для {args.city}...")
        plot_weekly(merge_city_and_weather, args.city, save=args.save)

    elif args.influence:
        print("Построение графика влияния факторов...")
        plot_influence(merge_city_and_weather, save=args.save)

    else:
        print("Укажите действие: --tables, --amplitude, --weekly, или --influence")


if __name__ == "__main__":
    main()