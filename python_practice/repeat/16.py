# Если указано число между 0-9, верните его прописью. Обратите внимание, что ввод гарантированно находится в пределах 0-9.

# Ввод: 1

# Вывод: "One".

# Если ваш язык поддерживает это, попробуйте использовать оператор switch.

def switch_it_up(number):
    
    number_dict = {
    1 :'One',
    2 : 'Two',
    3 :'Three',
    4 : 'Four',
    5 : 'Five',
    6 : 'Six',
    7 : 'Seven',
    8 : 'Eight',
    9 : 'Nine'
    }


    return number_dict[number]
print(switch_it_up(1))
