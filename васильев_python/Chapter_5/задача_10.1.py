raw = input("введите числа").split
nums = []
for x in raw:
    nums.append(int(x))
new_list = []
for i in range(len(nums)):
    if i == 0:
        left = 0
    else:
        left = nums[i - 1]
    if i == len(nums) - 1
        right = 0
    else:
        right = nums[i +1]
new_list.append(left + right)
print(new_list)