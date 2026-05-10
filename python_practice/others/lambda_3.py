user_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(map(lambda x: x * 2 if x % 2 == 0 else x * 3, user_list))
print(result)
