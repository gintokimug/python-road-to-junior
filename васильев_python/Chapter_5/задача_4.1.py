text = input(" Введите текст").split()
max_length = 0
for word in text:
    if len(word) > max_length:
        max_length = len(word)
print(max_length)

