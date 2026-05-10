# Базовый и самый долгий
def sum_two_smallest_numbers(numbers : list):
    numbers.sort()
    return   numbers[0] + numbers[1]

my_list  = [54, 21, 16, 7, 9]
print(sum_two_smallest_numbers(my_list))


# Через индексы
def sum_two_smallest_numbers(numbers):
    return sorted(numbers)[0] + sorted(numbers)[1]

# Через срезы
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])