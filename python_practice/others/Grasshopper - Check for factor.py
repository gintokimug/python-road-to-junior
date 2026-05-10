def check_for_factor(base, factor):
    if base % factor == 0:
        return True
    else:
        return False
print(check_for_factor(10, 2))

def check_for_factor(base, factor):
    return base % factor == 0