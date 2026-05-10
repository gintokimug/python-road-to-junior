# Ваш интернет-магазин любит раздавать купоны по особым случаям. Некоторые покупатели пытаются обмануть систему, вводя неверные коды или используя купоны с истекшим сроком действия.

# Задача
# Ваша миссия:
# Напишите функцию под названием checkCoupon, которая проверяет, действителен ли код купона и не истек ли срок его действия.

# Купон становится недействительным в день ПОСЛЕ истечения срока действия.
# Все даты будут передаваться в виде строк в следующем формате: "MONTH DATE, YEAR".
# Чтобы правильный и введенный коды совпадали, их значения и типы данных должны совпадать. Это означает, что, например, false и 0 — это не одно и то же, как и 123 и "123".
from datetime import datetime

def check_coupon(entered_code, correct_code, current_date: str, expiration_date: str) -> bool:
    if entered_code is not correct_code and entered_code != correct_code:
        if type(entered_code) != type(correct_code):
            return False

    fmt = "%B %d, %Y"
    cur = datetime.strptime(current_date, fmt)
    exp = datetime.strptime(expiration_date,fmt)

    return (entered_code == correct_code) and (type(entered_code) == type(correct_code)) and (cur <= exp)

    
