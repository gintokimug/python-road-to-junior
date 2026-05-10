# Является ли строка заглавной?
# Задача
# Создайте метод, который будет определять, является ли строка заглавной.

# Примеры (ввод -> вывод)
# "c" -> False
# "C" -> True
# "hello I AM DONALD" -> False
# "HELLO I AM DONALD" -> True
# "ACSKLDFJSgSKLDFJSKLDFJ" -> False
# "ACSKLDFJSGSKLDFJSKLDFJ" -> True
# В этой задаче строка считается написанной ЗАГЛАВНЫМИ БУКВАМИ, если в ней нет строчных букв. 
# Таким образом, любая строка, не содержащая букв, тривиально считается написанной ЗАГЛАВНЫМИ БУКВАМИ.

def is_uppercase(inp : str):
    new_inp : str = inp.upper()
    return new_inp == inp

example = 'hello i m donald'
print(is_uppercase(example))