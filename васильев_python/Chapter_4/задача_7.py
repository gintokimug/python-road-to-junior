text = input("Введите текст").lower()
dict_text = dict()
for letter in text:
    if letter in dict_text:
        dict_text[letter] += 1
    else:
        dict_text[letter] = 1
print(dict_text)

