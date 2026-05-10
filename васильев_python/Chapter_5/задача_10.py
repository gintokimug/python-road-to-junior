text = input("Введите текст")
words = text.split()
reversed_words = words[::-1]
print("".join(reversed_words))