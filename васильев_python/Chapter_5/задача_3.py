text = input("Введите текст")
result = ""
for char in text:
    num = ord(char)
    if 65 <= num <= 90: # большие буквы
        result += chr(num + 32)
    elif 97 <= num <= 122: # маленькие буквы
        result += chr(num - 32)
    else:
        result += char
print(result)


