txt = input("введите текст")
new_txt = ""
num = 0 
while num + 2 < len(txt):
    new_txt = txt[num +2] + txt[num +1] + txt[num]
    num += 3
if num < len(txt):
    new_txt += txt[num:]

print(new_txt)
