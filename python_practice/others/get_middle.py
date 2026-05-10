def get_middle(s):
    lenght = len(s)
    index = lenght // 2
    if lenght % 2 != 0:
        return s[index]
    else:
        return s[index - 1 : index + 1]
print(get_middle("loxok"))
print(get_middle("intertneto"))