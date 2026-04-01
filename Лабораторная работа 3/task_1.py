def product_finder(product_list, product) :
    if product in product_list :                        #если товар в списке, находим его индекс
        product_index = product_list.index(product)
    else:
        product_index = None                            #иначе значение индекса оставляем None
    return product_index


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = product_finder(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
