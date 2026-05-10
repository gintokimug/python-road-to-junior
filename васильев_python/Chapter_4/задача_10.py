dict_1 = {"a" : 10, "b" : 20, "c" : 30}
dict_2 = { "a" : 1, "b" : 20, "c" : 3}
new_dict = {}
for key in dict_1:
    if key in dict_2:
        value_set = {dict_1[key], dict_2[key]}
        new_dict[key] = value_set
print(new_dict)
        