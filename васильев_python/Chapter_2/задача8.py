days_of_week = {
    1: "Понедельник" ,
    2: "Вторник",
    3: "Среда",
    4: "Четверг",
    5: "Пятница",
    6: "Суббота",
    7: "Воскресенье" 
}
Number = int(input("Введите число от 1 до 7:"))
if Number in days_of_week:
    days_name = days_of_week[Number]
    print(f"день недели {days_name}")
else:
    print("ошибка")
