# Task
# You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.
# Examples
# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]



def sort_array(source_array):
    odd = []
    for num in source_array:
        if num % 2 != 0:
            odd.append(num)

    odd.sort()     
    j = 0

    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            source_array[i] = odd[j]
            j += 1
            
    return source_array

example = [5, 8, 6, 3, 4]
print(sort_array(example))


def sort_array(arr):
  odds = sorted((x for x in arr if x%2 != 0), reverse=True)
  return [x if x%2==0 else odds.pop() for x in arr]
