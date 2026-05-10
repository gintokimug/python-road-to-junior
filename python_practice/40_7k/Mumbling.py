# На этот раз никакой истории, никакой теории. В примерах ниже показано, как писать функции accum:

# Примеры:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"
# Параметр accum — это строка, содержащая только буквы из a..z и A..Z.

def accum(st):
    result = []

    for index, letter in enumerate(st, start= 0):
        point = (letter *(index +1)).capitalize()
        result.append(point)
    return "-".join(result)

example = ("abcd")
print(accum(example))


"""Возился с задачей чуть больше 2 часов, не мог сообразить как вклинить логику  цикла на написании нескольких букв одновременно.
   Важный косяк, снова пробую делать += ,когда нужно делать .append(), ЗАПОМНИ ЗАПОМНИ ЗАПОМНИ
   Встречал ранее, теперь осознанно , enumerate() ,где в цикле ты можешь  указываать элемент итерируемого объекта и  его индекс, в качестве аругементов
     1= сам объект, 
     2 = откуда стартуешь)
   
"""