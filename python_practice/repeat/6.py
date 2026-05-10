# Задача
# Вам дан массив чисел, верните сумму всех положительных чисел.

# Пример
# [1, -4, 7, 12] => 
# 1
# +
# 7
# +
# 12
# =
# 20
# 1+7+12=20
# Примечание
# . Если суммировать нечего, по умолчанию используется сумма 0.

def positive_sum(arr):
    result = 0
    # Your code here
    for num in arr:
        if num > 0:
            result += num
    return result 

example = [1, -4, 7, 12]
print(positive_sum(example))


