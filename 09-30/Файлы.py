file = open("text.txt")
list_in_file = file.readlines()
print(list_in_file)
for x in list_in_file:
    row_list = x.split()
    for k in range(len(row_list)):
    #запускаем цикл. будем прогоняться по списку, и сравнивать значения
        for i in range(k, len(row_list)):
    #сравниваем с оставшимися элементами и находим из них меньшее
            if int(row_list[i]) >= int(row_list[k]) and i != k:
                void_element = row_list[i]
                element_number  = i
            else:
                element_number = k
                void_element = row_list[k]
            row_list[element_number] = row_list[k]
            row_list[k] = void_element
    #меняю местами элементы
    print(*row_list)
