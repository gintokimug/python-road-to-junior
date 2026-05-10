n = int(input("введите число"))
if n < 0:
    print("ошибка")
else:
    fact = 1
for i in range(1, n + 1):
    fact *= i
    print("факториал", n, "число", fact)