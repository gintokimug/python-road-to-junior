def is_prime(n):
    if n < 2:
        return False
    # Проверяем делители от 2 до n-1
    for x in range(2, n):
        if n % x == 0:
            return False
    return True

# Тот самый диапазон от 1 до 100
result = []
for i in range(1, 101):
    if is_prime(i):
        result.append(i) # Действие: добавляем число в список

print(result)