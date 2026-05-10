# Пример задачи из учебника,нихуя не понял 
txt = input("введите текст")
new_txt = ""
num = 0 
while num<len(txt) - 1:
    new_txt = txt[num + 1] + txt[num]
    num += 2
    if num < len(txt):
        new_txt += txt[num]
        print ("\n результат \n вычисления", new_txt)  # и всё равно какая то ебанина, шиферы  ссаные 