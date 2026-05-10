# Задача
# Дано целое число. Определите, является ли оно квадратным числом:

# В математике квадратное число или полный квадрат — это целое число, являющееся квадратом другого целого числа, то есть произведение некоторого целого числа само на себя.

# В тестах всегда используется какое-то целое число, так что в языках с динамической типизацией об этом можно не беспокоиться.

# Примеры
# -1  =>  false
#  0  =>  true
#  3  =>  false
#  4  =>  true
# 25  =>  true
# 26  =>  false

# def is_square(n):
    
#     if n < 0 :
#         return  False
#     else:
#         for num in range(n):
#             if n == 0:
#                 return True
#             elif n == num*num:
#                 return True 
#             else:
#                 return False

# def is_square(n):
#     if n < 0:
#         return False
#     elif n == 0:
#         return True 
    
#     for num in range(n+1):
#         if n == num * num:
#             return True
#     return False 

def is_square(n):
    if n < 0: return False
    if n == 0: return True 

    root = n ** 0.5
    return root % 1 == 0



        

#  ПРОСТО 2 МОМЕНТА RETURN В ЦИКЛЕ FOR  ВСЕГДА НУЖНО СТАВИТЬ  НАРАВНЕ , НЕЛЬЗЯ ВНУТРИ, ОН НЕ  БУДЕТ ВЫХОДИТЬ, ЗАПОМНИ УЖЕ!!!!
#  ВТОРОЙ МОМЕНТ В  RANGE ВСЕГДА,ВСЕГДА,ВСГДА СТАВЬ + 1, ЧТОБЫ ВЗЯТЬ САМО ЧИСО ИНАЧЕ НЕ ВЫЙДЕТ, В ЗАДАЧЕ ЦИФРА 4 ШЛА ДО 3, Т.К ИНДЕКСАЦИЯ С 0 МАРТЫШ




example = 1
print(is_square(example))