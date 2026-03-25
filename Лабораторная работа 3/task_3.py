def find_common_participants(group_1, group_2, separator=",") :
#    for i in group_1 :          #ищем разделитель, а именно символ, не являющийся буквой
#       if not i.isalpha() :
#          separator = i
#          break
    students_1 = group_1.split(separator)       #разбиваем строку на фамилии по заданному разделителю
    students_2 = group_2.split(separator)
    common_list = students_1 + students_2           #создаём список из вссех фамилий
    for i in set(common_list):                      #и единожды удаляем оттуда каждую фамилию
        common_list.remove(i)

    return common_list


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))
