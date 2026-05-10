# Анаграмма — это результат перестановки букв в слове для получения нового слова (см. wikipedia).

# Примечание: анаграммы не чувствительны к регистру

# Дополните функцию так, чтобы она возвращала true в случае, если два указанных аргумента являются анаграммами друг друга, и false в противном случае.

# Примеры
# "foefet" является анаграммой "toffee"

# "Buckethead" является анаграммой "DeathCubeK"

# write the function is_anagram
def is_anagram(test, original):

    return sorted(test) == sorted(original)

    
    
#     if set(test.lower()) == set(original.lower()):
#         return True
#     else:
#         return False

example = "foefet"
original = "toffee"

print(is_anagram(example,original))