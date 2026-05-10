def pack_bag(*items):
    print(f"В сумке сейчас: {items}")
    print(f"Тип данных: {type(items)}")

# Мы передаем отдельные товары (перечисление)
pack_bag("Яблоки", "Хлеб", "Молоко")