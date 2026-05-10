n = int(input("введите число N:"))

for number in range(1, n):
    # Делится на 3 ИЛИ на 5
    is_divisible_by_3 = number % 3 == 0 
    is_divisible_by_5 = number % 5 == 0
    is_divisible_by_15 = number % 15 == 0
    
    if (is_divisible_by_3 or is_divisible_by_5) and not is_divisible_by_15:
        print(number)