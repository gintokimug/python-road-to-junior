vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
consonants = [
    'б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м',
    'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ'
]
text = input("Введите текст").lower()
result = ""
for char in text:
    if char in vowels:
        idx = vowels.index(char)
        if idx == len(vowels) -1:
            result += vowels[0]
        else:
            result += vowels[idx +1]
    elif char in consonants:
        idx = consonants.index(char)
        if idx == len(consonants) -1:
            result += consonants[0]
        else:
            result += consonants[idx +1]
    else:
        result += char
print(result)

