import random
import string

def create_char_matrix(rows, cols):
    """
    Создает вложенный список (матрицу) размером rows x cols,
    заполненный случайными строчными буквами английского алфавита.
    """
    # Получаем строку со всеми буквами: 'abcdef....z'
    alphabet = string.ascii_lowercase 
    
    # Генератор списка (List Comprehension)
    # Читать следует справа налево: Создаем список строк, повторяя это rows раз
    matrix = [
        [random.choice(alphabet) for _ in range(cols)] 
        for _ in range(rows)
    ]
    
    return matrix

# --- Тестируем функцию ---
# Запрашиваем размеры у пользователя
n_rows = int(input("Введите количество строк: "))
n_cols = int(input("Введите количество столбцов: "))

# Вызываем функцию
result_matrix = create_char_matrix(n_rows, n_cols)

# Красивый вывод (опционально, чтобы видеть структуру)
print("\nРезультат (сырой вид):")
print(result_matrix)

print("\nРезультат (красивый вид):")
for row in result_matrix:
    print(row)