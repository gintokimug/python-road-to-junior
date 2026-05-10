excluded_numbers = input("Введите список исключяющих числе через запятую: ").split(',')
upper_limit = int(input("Введите верхнуюю границу для вычисления суммы: "))
excluded_numbers = [int(num.strip()) for num in excluded_numbers]
total_sum = 0
for i in range(1, upper_limit + 1):
    if i not in excluded_numbers:
        total_sum +=  i 
print("Сумма натуральных чисел от 1 до ", upper_limit, "без учёта", excluded_numbers, "равна", total_sum)
