text = input("введите текстовое значение : ")
user_letter = dict()
for letter in text:
    if letter  not in user_letter:
        new_text = text.replace(letter,"")
        user_letter[letter] = new_text
print(user_letter)

