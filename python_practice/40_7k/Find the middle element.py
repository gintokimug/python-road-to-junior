# В рамках этой задачи вам нужно создать функцию, которая при получении тройки чисел возвращает индекс числового элемента, расположенного между двумя другими.

# На вход функции подается массив из трех различных чисел (в Haskell — кортеж).

# Например:

# gimme([2, 3, 1]) => 0
# 2 — это число, которое находится между 1 и 3, а индекс 2 во входном массиве — 0.

# Другой пример (просто чтобы было понятнее):

# gimme([5, 10, 14]) => 1
# 10 — это число, которое находится между 5 и 14, а индекс 10 во входном массиве равен 1.

def gimme(input_array):
    # Implement this function
    sorted_array = sorted(input_array)
    target = sorted_array[1]
    for num in range(len(input_array)):
        if input_array[num] == target:
            return num


def gimme(input_array):

    middle = sorted(input_array)[1]

    return input_array.index(middle)    



example = [2, 200, 100]
print(gimme(example))
