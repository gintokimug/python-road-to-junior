# Вам дана строка, и вы должны вернуть строку, в которой каждый символ (с учетом регистра) повторяется один раз.

# Примеры (ввод -> вывод):
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "

def double_char(s):
    result = ''
    for char in s:
        double_char = char + char
        result += double_char
    return result 


   

    





example = "Hello World"
print(double_char(example))