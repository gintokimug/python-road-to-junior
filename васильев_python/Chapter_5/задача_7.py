alphabet_ru = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphabet_en = "abcdefghijklmnopqrstuvwxyz"
text = "Я изучaю Python " 
result = ""
cipher_map = {}
for i in range(len(alphabet_ru)):
    char = alphabet_ru[i]
    target_char = alphabet_ru[i - 2]
    cipher_map[char] = target_char
for i in range(len(alphabet_en)):
    char = alphabet_en[i]
    target_char = alphabet_en[i - 2]
    cipher_map[char] = target_char
for char in text.lower():
    result += cipher_map.get(char, char)
print(result)


