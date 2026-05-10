text_1 = input("Введите текст")
text_2 = input("Введите текст")
limit = min(len(text_1), len(text_2))
result = ""
for i in range(limit):
    if i < len(text_1):
        result += text_1[i]
    else:
        result += "*"
    if i < len(text_2):
        result += text_2[i]
    else:
        result += "*"
print(result)
