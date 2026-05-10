import random
def weave_lists_classic(list_a, list_b):
    
    # создать новый список, поочередно добавляя элементы из списка а и b

    if len(list_a) != len(list_b):
        raise ValueError
    
    new_list = []
    n = len(list_a)
    for i in range(n):
        new_list.append(list_a[i])
        new_list.append(list_b[i])

    return new_list

# основная часть программы

LIST_SIZE = 5

list1 = [random.randint(1, 10) for _ in range(LIST_SIZE)]
list2 = [random.randint(11, 20) for _ in range(LIST_SIZE)]

print(f"Список А: {list1}")
print(f"Список B: {list2}")

# called func
result_classic = weave_lists_classic(list1, list2)

print(f"Результат: {result_classic}")