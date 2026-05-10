text_input = input("Введите любой текст")
original_turple = tuple(text_input)
print(f"Исходный кортеж:{original_turple}")
step = int(input("введите шаг (число):"))
new_purple = original_turple [::step]
print(f"Новый кортеж: {new_purple}")