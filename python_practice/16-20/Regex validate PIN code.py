# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

# If the function is passed a valid PIN string, return true, else return false.

# Examples (Input --> Output)
# "1234"   -->  true
# "12345"  -->  false
# "a234"   -->  false




def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        for char in pin:
            if char not in '0123456789':
                return False 
        return True
    return False


def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        return pin.isdigit()
    return False





example = '6666'
print(validate_pin(example))
    
