def printer_error(s):

    numerator = 0
    denominator = len(s)

    for letter in s:
        if letter > 'm':
            numerator += 1
    return f"{numerator}/{denominator}"

example = "aaabbbcccww"          
print(printer_error(example))
