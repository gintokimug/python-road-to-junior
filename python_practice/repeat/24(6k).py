# Запишите число в развернутом виде
# Вам будет дано число, которое нужно вернуть в виде строки в развернутом виде. Например:

#    12 --> "10 + 2"
#    45 --> "40 + 5"
# 70304 --> "70000 + 300 + 4"
# ПРИМЕЧАНИЕ: все числа должны быть целыми и больше 0.


def expanded_form(num : int):
    str_num = str(num)
    lenght = len(str_num)
    parts = []

    for i, digit in enumerate(str_num):
        if digit != '0':
            zero_count = lenght - i - 1
            current = digit + ('0' * zero_count)
            parts.append(current)
    return '+'.join(parts)

    
  

    


        


        




       
    

example = 70304
print(expanded_form(example))      