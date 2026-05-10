text = input("Введите текст").split()
filtered_words = []
for word in text: 
    if len(word) >= 3:
        filtered_words.append(word.capitalize())
result = "_". join(filtered_words)
print(result)

