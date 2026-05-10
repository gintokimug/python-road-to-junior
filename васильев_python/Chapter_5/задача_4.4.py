vowels = ["a", "e", "i", "o", "u", "y"]
text = "Python in awesome"
clean_text = ""
for char in text:
    if char.lower() not in vowels:
        clean_text += char
print(clean_text)
