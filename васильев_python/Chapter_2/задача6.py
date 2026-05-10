side_a = int(input("введите длину стороны (а): "))
side_b = int(input("введите длину стороны (b):"))
side_c = int(input("введите длину стороны (с)"))
cond_1 = side_a + side_b > side_c
cond_2 = side_b + side_c > side_a
cond_3 = side_c + side_a > side_b 
is_triangle = cond_1 and cond_2 and cond_3
if is_triangle:
    print("треугольник может быть")
else:
    print("треугольник не может быть ")