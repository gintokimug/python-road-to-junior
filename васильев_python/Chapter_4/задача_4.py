numbers = []
count = 51
for numb in range(1, count):
    if (numb % 3 == 0 or numb % 4 == 0) and not (numb % 3 == 0 and numb % 4 == 0):
        numbers.append(numb)
print(numbers)