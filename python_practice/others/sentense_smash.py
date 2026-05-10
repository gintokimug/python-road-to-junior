def smash(words): 
    sentence = ""
    for word in words:
        sentence += word + " "
    return sentence.strip()

words = ['hello', 'world', 'this', 'is', 'great']
print(smash(words))