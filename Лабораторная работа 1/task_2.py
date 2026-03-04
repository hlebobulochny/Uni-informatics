disk_value = 1.44  #исходные данные
pages = 100
strings = 50
symbols = 25
bytes_symbol = 4

disk_value_bytes = disk_value * 1024 * 1024  #переведём в байты

books = int(disk_value_bytes / (pages * strings * symbols * bytes_symbol)) #найдём целое количество книг с данными параметрами

print(f'Количество книг, помещающихся на дискету: {books}')
