numb = int(input("Введите число"))
a , b = 0, 1
result = []
while a < numb:
    result.append(a)
    a,b = b, a + b
print(result)


