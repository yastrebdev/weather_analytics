import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Weather Analysis CLI")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("--tables", action="store_true", help="Вывести агрегированные таблицы в консоль")
    group.add_argument("--amplitude", action="store_true", help="Построить график амплитуды по городам")
    group.add_argument("--weekly", action="store_true", help="Построить недельный график для города (--city)")
    group.add_argument("--influence", action="store_true", help="Показать график влияния факторов на температуру")

    parser.add_argument("--city", type=str, help="Название города (для --weekly)")
    parser.add_argument("--save", action="store_true", help="Сохранить график в файл вместо показа")

    return parser.parse_args()