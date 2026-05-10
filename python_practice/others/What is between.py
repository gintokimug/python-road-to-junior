def between(a,b):
    my_list = []
    while a <= b:
        my_list.append(a) 
        a += 1
    return my_list

print(between(1,4))
