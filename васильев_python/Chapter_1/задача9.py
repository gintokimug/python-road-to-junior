def spisok(numbers):
    u_numbers = list(set(numbers))
    if len(u_numbers) < 2:
        return None
    u_numbers.sort()
    return u_numbers[-2]
input_list = [4, 66, 43, 26, 55]
result = spisok(input_list)
if result is not None:
        print("Второе по величине число", result)
else:
     print ("В списке нет уникальных числе")