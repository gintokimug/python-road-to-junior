import random

# --- Блок вспомогательных функций (Helpers) ---

def create_matrix(rows, cols):
    """Генерирует матрицу rows x cols со случайными числами."""
    # Используем List Comprehension — это стандарт индустрии
    return [[random.randint(10, 99) for _ in range(cols)] for _ in range(rows)]

def print_matrix(matrix):
    """Выводит матрицу ровными рядами."""
    if not matrix:
        print("Матрица пуста!")
        return
    for row in matrix:
        # f"{x:3}" добавляет пробелы, чтобы числа стояли ровно
        print(" ".join(f"{x:3}" for x in row))

# --- Блок основной логики (Core Logic) ---

def delete_row_col(matrix, row_idx, col_idx):
    """
    Удаляет строку и столбец по индексам.
    Улучшенная версия с поддержкой отрицательных индексов.
    """
    
    current_rows = len(matrix)
    
    # 1. Удаляем СТРОКУ
    # Допустимые индексы: от -N до N-1
    if -current_rows <= row_idx < current_rows:
        matrix.pop(row_idx) 
        print(f"✅ Удалена строка под индексом {row_idx}.")
    else:
        print(f"❌ Ошибка: Строки {row_idx} не существует. Пропускаем.")
        return # Если строка не удалена, нет смысла удалять столбец

    # 2. Удаляем СТОЛБЕЦ
    # Проверка, что матрица не пуста, и индекс столбца допустим
    if len(matrix) > 0:
        current_cols = len(matrix[0])
        if -current_cols <= col_idx < current_cols:
            for row in matrix:
                row.pop(col_idx)
            print(f"✅ Удален столбец под индексом {col_idx}.")
        else:
            print(f"❌ Ошибка: Столбца {col_idx} не существует. Пропускаем.")
    # else: Матрица пуста, делать нечего

# --- Точка входа (Main execution) ---

# Параметры
N = 4 # Строки
M = 5 # Столбцы

# Инициализация
my_data = create_matrix(N, M)

print("--- ДО ---")
print_matrix(my_data)

# Ввод данных (сразу оборачиваем в int)
try:
    del_r = int(input("\nКакую строку удалить (индекс)? "))
    del_c = int(input("Какой столбец удалить (индекс)? "))

    # Выполнение
    delete_row_col(my_data, del_r, del_c)

    print("\n--- ПОСЛЕ ---")
    print_matrix(my_data)

except ValueError:
    print("\nНужно вводить целые числа!")