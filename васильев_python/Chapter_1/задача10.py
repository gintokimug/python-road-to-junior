def sum_of_odds(count):
    total_sum = 0
    for i in range(1, count + 1):
        if i % 2 != 0:
            total_sum += i
    return total_sum
number = int(input("введите количество чисел"))
result = sum_of_odds(number)
print("Сумма нечётных чисел от 1 до ", number, "равна", result)