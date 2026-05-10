text = input("Введите текст")

words = text.split()
if len(words) > 0:
    longest = max(words, key= len)
    shortest = min(words, key = len)
    words.remove(longest)
    words.remove(shortest)
new_text= " ".join(words)
print(new_text)


