text = "фнпб мфнпб"
result = ""
for char in text:
    if "а" <= char <= "я":
        if char == "а":
            result += "я"
        else:
            result += chr(ord(char) - 1)
    elif "А" <= char <= "Я":
        if char == "А":
            reslut += "Я"
        else:
            result += chr(ord(char) -1)
print(result)
