# Даны два числа и арифметический оператор (его название в виде строки). Верните результат применения этого оператора к двум числам.

# a и b оба будут целыми положительными числами, и a всегда будет первым числом в операции и b всегда вторым.

# Четыре оператора - это "сложение", "вычитание", "деление", "умножение".

# Несколько примеров: (Вход1, Вход2, Вход3 --> Вывод)

# 5, 2, "add"      --> 7
# 5, 2, "subtract" --> 3
# 5, 2, "multiply" --> 10
# 5, 2, "divide"   --> 2.5
# Попробуйте сделать это без использования операторов if!

def arithmetic(a, b, operator):

    # В данном случае использование словарей куда эффективнее, нежели  кучка  if, работе со словарями ужно уделить больше внимания
    dictionaty = { 
                'add': a + b,
                'subtract': a - b,
                'multiply': a * b,
                'divide': a /b
                     }
    return dictionaty[operator]

    
    # if operator == 'add':
    #     return a + b
    # elif operator == 'subtract':
    #     return a - b
    # elif operator == 'multiply':
    #     return a * b
    # elif operator == 'divide':
    #     return a / b
    

a = 5
b = 2
operator = '*'
print(arithmetic(a,b,operator))