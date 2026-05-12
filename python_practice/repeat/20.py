# Можете ли вы найти иголку в стоге сена?

# Напишите функцию, findNeedle() которая принимает array полный мусор, но содержащую "needle"

# После того, как ваша функция найдет иглу, она должна вернуть сообщение (в виде строки), в котором говорится:

# "found the needle at position " плюс index она нашла иглу, так что:

# Пример (Ввод -> Вывод)

# ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at position 5" 
# Примечание: в COBOL функция должна возвращать "found the needle at position 6"

def find_needle(haystack):
     
    return f"found the needle at position {haystack.index('needle')}"
    

example = ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]
print(find_needle(example))