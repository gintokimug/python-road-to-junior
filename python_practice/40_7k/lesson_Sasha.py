"""Создать парсер.
Изначально равно 0.

Парсер использует четыре односимвольные команды:

i: Увеличить значение
d: Уменьшить значение
s: Возвести значение в квадрат
o: Вывести значение в массив(список) результатов

Любая другая инструкция — это операции без эффекта

Примеры
1. Ввод в парсер строки "siiidoso" должен вернуть числа [8, 64]. 
2. Ввод в парсер строки "iiisdosodddddiso" должен вернуть числа [8, 64, 3600].
"""


"""
def fixed_tests():
    @test.it("Some examples")
    def tests():
        test.assert_equals(parse("ooo"), [0,0,0])
        test.assert_equals(parse("ioioio"), [1,2,3])
        test.assert_equals(parse("idoiido"), [0,1])
        test.assert_equals(parse("isoisoiso"), [1,4,25])
"""


def parser(text: str):
    result : list  = [] 
    x : int = 0 
    i : int = x + 1
    d : int = x - 1
    s : int  = x ** 2
    # o : None  = result.append(x)
    
    for char in text:
        if char == 'i':
            x += 1
        elif char == 's':
            x **= 2
        elif char == 'd':
            x -= 1
        elif char == 'o':
            result.append(x)
        
    return result

example = "isoisoiso"
print(parser(example)) 




"""Создать парсер.
Изначально равно 0.

Парсер использует четыре односимвольные команды:

i: Увеличить значение
d: Уменьшить значение
s: Возвести значение в квадрат
o: Вывести значение в массив результатов

Любая другая инструкция — это операции без эффекта

Примеры
1. Ввод в парсер строки "iiisdoso" должен вернуть числа [8, 64]. 
2. Ввод в парсер строки "iiisdosodddddiso" должен вернуть числа [8, 64, 3600].
"""


"""
def fixed_tests():
    def tests():
        test.assert_equals(parse("ooo"), [0,0,0])
        test.assert_equals(parse("ioioio"), [1,2,3])
        test.assert_equals(parse("idoiido"), [0,1])
        test.assert_equals(parse("isoisoiso"), [1,4,25])
"""



        
        

        
# Create a function taking a positive integer between 1 and 3999 (both included) as its parameter and returning a string containing the Roman Numeral representation of that integer.


# Modern Roman numerals are written by expressing each digit separately starting with the leftmost digit and skipping any digit with a value of zero. 
# There cannot be more than 3 identical symbols in a row.

# In Roman numerals:

# 1990 is rendered: 1000=M + 900=CM + 90=XC; resulting in MCMXC.
# 2008 is written as 2000=MM, 8=VIII; or MMVIII.
# 1666 uses each Roman symbol in descending order: MDCLXVI.

# Example:
# 1 -->       "I"
# 1000 -->       "M"
# 1666 --> "MDCLXVI"

# Help:

# Symbol    Value
# I          1
# V          5
# X          10
# L          50
# C          100
# D          500
# M          1,000