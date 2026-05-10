# Джейден Смит, сын Уилла Смита, снялся в таких фильмах, как «Каратэ-пацан» (2010) и «После Земли» (2013).
#  Джейден также известен своими философскими высказываниями, которые он публикует в Twitter. В Twitter он почти всегда пишет с заглавной буквы каждое слово. 
# Для простоты вам тоже придется писать каждое слово с заглавной буквы. Посмотрите, как в примере ниже сокращаются слова.
# Ваша задача — преобразовать строки так, как их написал бы Джейден Смит. Строки — это реальные цитаты Джейдена Смита, но они написаны не с заглавной буквы, как он.
# Пример:
# Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
# Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"

def to_jaden_case(string):

    words= string.split()
    result = []

    for word in words:
        result.append(word.capitalize())
    return "".join(result)



        
    

example = "hello python ff jj jkk ii iyy hqw"
print(to_jaden_case(example))
