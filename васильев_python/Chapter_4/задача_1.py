import random

numbers = []

for _ in range(5):
    numbers.append(random.randint(1, 10))

for _ in range(10):
    numbers.append(random.randint(10, 30))
print(numbers)
