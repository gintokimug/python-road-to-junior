num_a = int(input("Введите первое целое число: "))
num_b = int(input("Введите второе целое число:"))
num_c = int(input("Введите третье целое число: "))
diff_1 = num_b - num_a
diff_2 = num_c - num_b
is_arith = diff_1 == diff_2
if is_arith:
    print( f" числа {num_a}, {num_b}, {num_c} являются числами прогрессии с разностью {diff_1}")
else:
    print( f"числа {num_a}, {num_b}, {num_c} не являются числами прогрессии")