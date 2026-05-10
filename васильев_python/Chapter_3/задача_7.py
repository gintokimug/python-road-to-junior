def get_max_element_details(data_list):
    """
    Находит наибольший элемент в списке и индекс его ПЕРВОГО вхождения.
    
    Аргумент: data_list (list)
    Возвращает: list [максимальное значение, индекс]
    """
    
    # --- Защита от "Краевого случая" (Empty List) ---
    if not data_list:
        print("Ошибка: Список пуст.")
        return [None, None]
        
    # 1. Инициализация (Предполагаем, что первый элемент — максимальный)
    max_value = data_list[0]
    max_index = 0
    
    # 2. Итерируем, используя enumerate (дает ИНДЕКС (i) и ЗНАЧЕНИЕ (current_value))
    # Мы начинаем цикл со второго элемента (индекс 1), так как 0-й уже проверен
    for i, current_value in enumerate(data_list):
        
        # 3. Ключевая логика: Сравнение
        # Используем СТРОГОЕ сравнение (>), чтобы обеспечить "правило первого вхождения".
        if current_value > max_value:
            
            # Найдено новое, большее значение!
            max_value = current_value
            max_index = i
            
        # else: Если current_value == max_value, мы НЕ ОБНОВЛЯЕМ max_index,
        # тем самым сохраняя индекс первого найденного максимального элемента.
            
    return [max_value, max_index]

# --- Тест ---
list_a = [10, 99, 50, 99, 25] # Максимум 99, встречается дважды.
list_b = [-5, -1, -10, 0]

result_a = get_max_element_details(list_a)
result_b = get_max_element_details(list_b)

print(f"Список: {list_a} -> Максимум: {result_a[0]}, Индекс: {result_a[1]}")
print(f"Список: {list_b} -> Максимум: {result_b[0]}, Индекс: {result_b[1]}")