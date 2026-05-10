# Возьмите 2 строки s1 и s2 и оставьте в них только буквы от a до z.
#  Верните новую отсортированную строку 
# (в алфавитном порядке по возрастанию), максимально длинную, содержащую уникальные буквы из s1 или s2, каждая из которых встречается только один раз.

# Примеры:
# a = "xyaabbbccccdefww"
# b = "xxxxyyyyabklmopq"
# longest(a, b) -> "abcdefklmopqwxy"

# a = "abcdefghijklmnopqrstuvwxyz"
# longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

def longest(a1, a2):
    
    set1 = set(a1)
    set2 = set(a2)
   

    s3 = set1.union(set2)
    sorted_set = "".join(sorted(s3))
    return sorted_set
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"    

print(longest(a,b))

"""Помогло знание, что для объединения уникальных элементов в один список, можно использовать set(),union or | .
  Ещё раз, более осмысленно, sorted() работает со всеми типами контейнеров(списки, кортежи,множества), типо внутри без разницы , дальше уже по знакому примеру .join"""
        




