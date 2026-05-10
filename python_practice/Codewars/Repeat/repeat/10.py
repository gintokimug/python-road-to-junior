# Описание:
# Напишите функцию bmi, которая вычисляет индекс массы тела (bmi = вес / рост2).

# если bmi <= 18,5, верните "Недостаточный вес".

# если ИМТ <= 25,0, верните "Нормальный"

# если ИМТ <= 30,0, верните "Избыточный вес"

# если ИМТ > 30, верните "Ожирение"

def bmi(weight, height):
    imt = weight / height ** 2
    if imt <= 18.5:
        return "Underweight"
    elif imt <= 25:
        return "Normal"
    elif imt <= 30:
        return "Overweight"
    elif imt > 30:
        return "Obese"