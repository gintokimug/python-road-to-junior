pairs = set()

for i in range(1, 21, 2):
    first = i
    second = i + 2
    new_tuple = (first, second)
    pairs.add(new_tuple)
print(pairs)