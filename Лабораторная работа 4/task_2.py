import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    list_ = []        #список для словарей значений
    with open(INPUT_FILENAME, "r") as file:         #читаем из файла в словари по строкам
        reader = csv.DictReader(file)
        for row in reader:                          #полученные словари добавляем в список и формируем весь объём данных
            list_.append(row)

    with open(OUTPUT_FILENAME, "w") as file :       #записываем в файл полученный список
        json.dump(list_, file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")