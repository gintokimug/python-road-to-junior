def create_spiral_matrix(rows, cols):
    # 1. Создаем пустую матрицу, заполненную нулями
    # Мы используем генератор, который ты уже изучил
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # 2. Устанавливаем начальное число
    num = 1
    
    # 3. Определяем границы (стены)
    top = 0
    bottom = rows - 1
    left = 0
    right = cols - 1
    
    # Максимальное число, которое мы должны вписать
    max_num = rows * cols
    
    # 4. Главный цикл: пока не заполним все ячейки
    while num <= max_num:
        
        # --- Движение ВПРАВО (по верхней границе) ---
        # Идем от левой стены до правой (включительно)
        for i in range(left, right + 1):
            if num <= max_num:
                matrix[top][i] = num
                num += 1
        top += 1 # Сдвигаем "потолок" вниз
        
        # --- Движение ВНИЗ (по правой границе) ---
        # Идем от верхней границы до нижней
        for i in range(top, bottom + 1):
            if num <= max_num:
                matrix[i][right] = num
                num += 1
        right -= 1 # Сдвигаем правую стену влево
        
        # --- Движение ВЛЕВО (по нижней границе) ---
        # Идем от правой границы до левой (шаг -1)
        for i in range(right, left - 1, -1):
            if num <= max_num:
                matrix[bottom][i] = num
                num += 1
        bottom -= 1 # Поднимаем "пол" вверх
        
        # --- Движение ВВЕРХ (по левой границе) ---
        # Идем от нижней границы до верхней (шаг -1)
        for i in range(bottom, top - 1, -1):
            if num <= max_num:
                matrix[i][left] = num
                num += 1
        left += 1 # Сдвигаем левую стену вправо

    return matrix

# --- Тестируем ---
n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))

spiral = create_spiral_matrix(n, m)

print("\nРезультат:")
for row in spiral:
    # Трюк для красивого вывода: форматирование строк
    # Каждое число занимает 4 символа
    print(" ".join(f"{x:4}" for x in row))

    