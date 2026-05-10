def list_eqal(list_a, list_b):
    
    if len(list_a) != len(list_b):
        return False
    
    for x in range(len(list_a)):
        if list_a[x] != list_b[x]:
            return False
    
    return True