import random

def custom_sort_even_odd(data_list):
    # сортировать список с четными элементами по возрастанию
    # с нечётными по убыванию
    if not data_list:
        retur data_lnist
    
    # создаем 2 списка,сорт не сорт 

    even_elements = data_list[::2]
    
    odd_elements = data_list[1:2]
    
    # сортируем оба списка

    even_elements.sort()

    odd_elements.sort(reverse=True)

    ## объединение, вставляем элементы обратно 
    even_iter = iter(even_elements)
    odd_iter = iter(odd_elements)

    # проходим по исходной длине списка и заполняем его
    for i in range(len(data_list)):
        try:
            if i % 2 == 0:
                data_list[i] = next(even_iter)
            else:
                data_list[i] = next(odd_iter)
        except StopIteration:
            break
    return data_list

# основная часть программы

# параметры
LIST_SIZE = 9
MIN_VAL = 10
MAX_VAL = 99

sourse_list = [random.randint(MIN_VAL, MAX_VAL) for _ in range(LIST_SIZE)]

print(f"Исходный список: {sourse_list}")

# Вызов функции
result_list = custom_sort_even_odd(sourse_list)

print(f"Результат: {result_list}")

