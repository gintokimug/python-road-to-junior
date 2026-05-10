number = int(input("введите число"))
original = list(range(number + 1))
reversed_list = original[::-1]
result_dict = {}
for i in range(len(original)):
    key = original[i]
    value = reversed_list[i]
    result_dict[key] = value
print(f"результ {result_dict}")

