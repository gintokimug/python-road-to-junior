# Вам будет дан список строк. Вы должны отсортировать его в алфавитном порядке (с учетом регистра и на основе значений ASCII символов), а затем вывести первое значение.

# Возвращаемое значение должно быть строкой с символами "***" между буквами.

# Не удаляйте и не добавляйте элементы в массив.



def two_sort(array):
    # your code here
    sort_array = sorted(array)

    return '***'.join(sort_array[0])
    print(array)
    print(sort_array) 

example = ["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]
print(two_sort(example))