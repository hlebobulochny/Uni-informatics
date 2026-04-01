import json

# TODO решите задачу
def task(json_file) -> float:
    summary = 0             #переменная для подсчёта суммы

    with open(json_file) as file :          #читаем данные из файла в переменную
        data = json.load(file)

    for dictionary in data :                                    #проходимся по словарям из файла и в каждом по ключам получаем
        summary += dictionary['score'] * dictionary['weight']   #значения score и weight, которые перемножаем и прибавляем к нашей сумме

    return round(summary, 3)        #возвращаем полученную сумму, округлённую до 3 знаков

print(task("input.json"))
