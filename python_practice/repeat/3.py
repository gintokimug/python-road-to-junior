# Напишите функцию, которая преобразует имя в инициалы.
#  В этой задаче нужно использовать только два слова, разделенных пробелом.

# На выходе должны получиться две заглавные буквы, разделенные точкой.

# Должно получиться так:

# Sam Harris => S.H

# patrick feeney => P.F

def abbrev_name(name : str):
    words = name.split()
    word_1 = words[0]
    word_2 = words[1]
    word_3 = word_1[0].upper() + word_2[0].upper()
    return ".".join(word_3)


    # return ".".join(w[0] for w in name.split()).upper()

example = 'Sam Harris'
print(abbrev_name(example))
    
    
