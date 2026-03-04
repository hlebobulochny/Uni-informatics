numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
gap_index = -1 #введём индекс пропуска

for k, elem in enumerate(numbers) : #найдём пропуск и его индекс в списке(можно через метод .index())
    if elem is None :   #если элемент равен None, запишем его индекс в переменную
        gap_index = k
        break  #выйдем из цикла, если нашли нужный элемент

summ = sum(numbers[:gap_index]) + sum(numbers[gap_index+1:])  #найдём сумму элементов, не включая пропуск
length = len(numbers) #длина списка
numbers[gap_index] = summ / length #на место пропуска запишем среднее арифметическое

print(f'Измененный список: {numbers}')

