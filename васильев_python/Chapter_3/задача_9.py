import random

def number_list_sorted(original_list):

    if not original_list:

        return []

    new_list = []
    l = len(original_list)

    for i in range(l - 1):
        current_element = original_list[i]

        next_element = original_list[i + 1]

        new_list.append(current_element)

        sum_of_neighbors = current_element + next_element

        new_list.append(sum_of_neighbors)

    # добавляем последний элемент исходного списка
    # последний элемент не имеет соседа справа, поэтому он остается за пределами списка
    new_list.append(original_list[l - 1])

    return new_list


# основная часть программы

# создание исходного спика
list_size = 5

sourse_list = [random.randint(1, 10) for _ in range(list_size)]

print(f"Исходный список: {sourse_list}")

# вызов функции
result_list = number_list_sorted(sourse_list)

print(f"Результат: {result_list}")



