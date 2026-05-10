def basic_op(operator, value1, value2):
    
    if operator == '+':
        return  value1 + value2
    elif operator == '-':
        return  value1 - value2
    elif operator == '*':
        return value1 * value2
    elif operator == '/':
        return value1 / value2
    
print(basic_op('+', 4, 7))
print(basic_op('-', 15, 18))
print(basic_op('*', 5, 5))
print(basic_op('/', 49, 7))

def basic_op(operator, v1, v2):

    ops = {'+' : v1 + v2 , '-' : v1 - 2 , '*' : v1 * v2 , '/' : v1 / v2}
    return ops[operator]  