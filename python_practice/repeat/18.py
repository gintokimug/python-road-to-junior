# Напишите функцию, которая возвращает значение, умноженное на 50 и увеличенное на 6. Если введенное значение является строкой, функция должна вернуть «Ошибка».

def problem(a):
    #Easy Points ^_^
    if a ==  str(a):
        return "Error"
    else:
        return  a * 50 + 6
    

example = 1
print(problem(example))