numbers = []
for i in range(18):
    if i % 5 == 3:
        numbers.append(i)
print("список в прямом порядке", numbers)
print("список в обрятном порядке", list(reversed(numbers)))