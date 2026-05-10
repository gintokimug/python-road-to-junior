from random import randint

nums = []

total = 10

for _ in range(total):
        num = randint(1, 10)
        if num % 2 == 0:
            correct_num = randint(2, 10)
        else:
            correct_num = randint(1, 9)

        nums.append(correct_num)

print(nums)


