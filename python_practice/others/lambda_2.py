user_text = input("Введите текст")
digit = '0123456789'
result = list(filter(lambda x : x in digit, user_text))
print(result)