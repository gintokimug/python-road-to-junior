# Ваша задача — написать функцию, которая возвращает сумму последовательности целых чисел.

# Последовательность определяется тремя неотрицательными значениями: начало, конец, шаг.

# Если значение begin больше, чем end, ваша функция должна вернуть 0. 
#   Если end не является результатом целочисленного количества шагов, не добавляйте его к сумме. См. четвертый пример ниже.

# Примеры

# 2,2,2 --> 2
# 2,6,2 --> 12 (2 + 4 + 6)
# 1,5,1 --> 15 (1 + 2 + 3 + 4 + 5)
# 1,5,3  --> 5 (1 + 4)
# Это первая ката в серии:

# Сумма последовательности (это ката)
# Сумма последовательности [сложная версия]

def sequence_sum(begin_number, end_number, step):
    #your code here
    if begin_number > end_number:
                return 0
    summa = 0
    for num in range(begin_number,end_number,step):
            summa += num
    return summa

def sequence_sum(begin_number, end_number, step):
        return sum(range(begin_number, end_number + 1, step))

example = 1,5,1

print(sequence_sum(example))
                
                



