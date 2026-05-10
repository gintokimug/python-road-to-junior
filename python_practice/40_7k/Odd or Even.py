# Задача:
# Дан список целых чисел. Определите, является ли сумма его элементов нечетной или четной.

# Приведите ответ в виде строки, соответствующей "odd" или "even".

# Если входной массив пуст, считайте, что он имеет вид: [0] (массив с нулем).

# Примеры:
# Input: [0]
# Output: "even"

# Input: [0, 1, 4]
# Output: "odd"

# Input: [0, -1, -5]
# Output: "even"
# Получайте удовольствие!


# def odd_or_even(arr):

#         if sum(arr) // 2 == 0:
#             print("odd")
#         else:
#             print("even")

# example = [0]    
# print(odd_or_even(example))        


def odd_or_even(arr):

    sumarr = sum(arr)
    if sumarr % 2 == 0:
        return "even"
    else:
        return "odd"
    
example = [0, 2, 5, 2]    
print(odd_or_even(example))     




