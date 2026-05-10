# Вам дано случайное неотрицательное число, и вы должны вернуть его цифры в обратном порядке в виде массива.

# Пример (ввод => вывод):
# 35231 => [1,3,2,5,3]
# 0     => [0]
def digitize(n : int):
    # result = []
    # str_n = str(n)
    
    # for num in reversed(str_n):
    #     result.append(int(num))
    # return result
    
    result : list = []
    for num in reversed(str(n)):
        result.append(int(num))
    return result


    


 

    
    

example = 35231
print(digitize(example))