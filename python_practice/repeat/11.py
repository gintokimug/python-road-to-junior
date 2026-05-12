# Описание:
# Напишите функцию, которая принимает в качестве аргумента список строк и возвращает отфильтрованный список, содержащий те же элементы, но без слова «гуси».

# Гуси — это любые строки из следующего массива, который уже заполнен в вашем решении:

#   ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
# Например, если бы этот массив был передан в качестве аргумента:

#  ["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]
# Ваша функция вернет следующий массив:

# ["Mallard", "Hook Bill", "Crested", "Blue Swedish"]
# Элементы в возвращаемом массиве должны располагаться в том же порядке, что и в исходном массиве, переданном в вашу функцию, но без слова 'geese'.
#  Обратите внимание, что все строки будут в том же регистре, что и исходные, а некоторые элементы могут повторяться.

geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    #your code here
    result = []
    for word in birds:
        if word not in geese:
            result.append(word)
    return result

example = ["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]
print(goose_filter(example))

