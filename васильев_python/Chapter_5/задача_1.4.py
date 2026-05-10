email = input("Введите электронную почту")
if "@" in email and email.endswith((".ru", ".com")):
    print("Почта корректна")
else:
    print("Ошибка в адресе")
    