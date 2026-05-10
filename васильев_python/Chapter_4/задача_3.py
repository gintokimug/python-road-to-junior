vowels = set("аеёиоуыэюя")
text = input("введите текст")
result = set(text)
res = result & vowels 
print(f"{res}")