try:
    a = float(input("введите первое действительное число:"))
    b = float(input("введите второе действительное число"))
    result = "a больше b" if a > b else "B больше или равно A"
    print(f"результат сравнения: {result}")
except ValueError:
    print("ошибка")
    