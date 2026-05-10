# Создайте функцию с именем divisors/Divisors , которая принимает целое число n > 1 и возвращает массив со всеми делителями этого числа 
# (кроме 1 и самого числа), от наименьшего к наибольшему.
#  Если число простое, верните строку «(целое число) простое» (null в C#, пустая таблица в COBOL) (используйте Either String a в Haskell и Result<Vec<u32>, String> в Rust).

# Примеры:
# divisors(12) --> [2, 3, 4, 6]
# divisors(25) --> [5]
# divisors(13) --> "13 is prime"

def divisors(integer):
    result = []
    for x in range(2, integer):
        if integer % x == 0:
            result.append(x)
    if not result:
        return f'{integer} is prime'

    return result
    
example = 12
print(divisors(example))


"""1 ошибка была в выставлении границ range, надо было брать от 2 до переменной, потому что по условиям задачи. Так же ошибка в выборе делителя/делимого, казуально, не забывай
Напомню себе ещё раз про .append(), метод работает с списками."""