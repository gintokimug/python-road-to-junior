# В строке с цифрами нужно заменить все цифры меньше 5 на '0', а все цифры 5 и выше — на '1'. Верните полученную строку.

# Примечание: input никогда не будет пустой строкой

def fake_bin(x : str):
    
    result = ''
    for num in x:
        if int(num) < 5:
            result += '0'
        else:
            result += '1'
    return result
            

example = "45385593107843568"
print(fake_bin(example))