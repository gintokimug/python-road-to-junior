# Создайте функцию, которая возвращает массив целых чисел от n до 1, где n>0.

# Пример: n=5 --> [5,4,3,2,1]

def reverse_seq(n):
    result = []
    for number in range(0,n + 1):
        if number <= n:
            result.append(number)
    return result[::-1]
    
example = 5
print(reverse_seq(example))