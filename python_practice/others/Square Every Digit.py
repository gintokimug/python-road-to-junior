def square_digits(num):
    
    result = ""
    for digit in str(num):
        square = int(digit) ** 2
        result += str(square)
    return int(result)

    


def square_digits(num):
    return int("".join(str(int(x)** 2) for x in str(num)))   




example = 123
print(square_digits(example))