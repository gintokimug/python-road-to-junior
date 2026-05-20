# Для заданного непустого массива целых чисел верните результат перемножения значений в порядке их следования. Пример:

# [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24

def grow(arr):
    result = 0
    for num in arr:
        result += result * num
    return result


example = [1, 2, 3, 4]
print(grow(example))
    
