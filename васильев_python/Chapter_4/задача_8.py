books_dict = { 
    "Мартин" : "Игра престолов",
    "Драйзер" : "Финансист", 
    "Сервантес" : "Дон Кихот" ,
     "Акутами" : "Магическая битва",
    "Герберт" : "Дюна"
}
correct_answer = 0
for author, book in books_dict.items():
    print(f"Кто написал произведение {book}")
    answer = input("Введите фамилию автора")
    if answer.lower() == author.lower():
        print("Верно")
        correct_answer += 1
    else:
        print(f"Ошибка.Правильный ответ: {author}")
print(f"Конец. Ваш результат{correct_answer}")