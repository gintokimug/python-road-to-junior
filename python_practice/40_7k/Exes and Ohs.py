# роверьте, одинаковое ли количество символов 'x' и 'o' в строке. Метод должен возвращатьлогическое значение и не учитывать регистр. Строка может содержатьлюбые символы.

# Примеры ввода/вывода:

# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false

# def xo(s):
#     s = str(s).lower()

#     if  s.count("x") != s.count("o"):
#         return False
#     else:
#         return True

def xo(s):
    s.lower()
    return (s.count('x') == s.count('o'))


example_1 = "xoXoxo"
example_2 = "xxxooOooxoxoxoxox"
print(xo(example_1))
