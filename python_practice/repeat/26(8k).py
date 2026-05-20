# Напишите функцию, которая возвращает строку, в которой имя заменено на фамилию.

# Пример (Ввод -> Вывод)

# "john McClane" --> "McClane john"

def name_shuffler(str_ : str):
    new_str = str_.split()
    x = new_str[0], new_str[1] = new_str[1], new_str[0]
    return ' '.join(x)
    



example = "john McClane"
print(name_shuffler(example))