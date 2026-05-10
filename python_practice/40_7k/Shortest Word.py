# Простая задача: для заданной строки слов вернуть длину самого короткого слова (слов).

# Строка никогда не будет пустой, и вам не нужно учитывать различные типы данных.

def find_short(s):
    # your code here
    words = s.split()
    min_len = len(words[0])
    for word in words:
        if len(word) < min_len:
            min_len = len(word)
    return min_len

                                                                
    
example = "bitcoin take over the world maybe who knows perhaps"
print(find_short(example))

"""для сравнения слов на их длину нужно использовать .split(), так он разбивает целую строку на отдельные слова по которой можно пройтись циклом с помощью len()
      Так же необходимо всегда заводить переменную для сравнения,куда  ты будешь класть в последствии что либо , это  МАСТ ХЕВ, разумеется есть решение однострочное 
      return min(len(word) for word in s.split())"""