# def caesar(text, shift, encrypt=True):

#     if not isinstance(shift, int):
#         return 'Shift must be an integer value.'

#     if shift < 1 or shift > 25:
#         return 'Shift must be an integer between 1 and 25.'

#     alphabet = 'abcdefghijklmnopqrstuvwxyz'

#     if not encrypt:
#         shift = - shift
    
#     shifted_alphabet = alphabet[shift:] + alphabet[:shift]
#     translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
#     encrypted_text = text.translate(translation_table)
#     return encrypted_text

# def encrypt(text, shift):
#     return caesar(text, shift)
    
# def decrypt(text, shift):
#     return caesar(text, shift, encrypt=False)

# encrypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf.'
# decrypted_text = decrypt(encrypted_text, 13)
# print(decrypted_text)
# print(encrypted_text)

# full_dot = '●'
# empty_dot = '○'

# def create_character(name, STR, INT, CHA):
#     if type(name) is not str:
#         return "The character name should be a string."
    
#     if name == '':
#         return "The character should have a name."
    
#     if len(name) > 10:
#         return "The character name is too long."
    
#     if  ' ' in name:
#         return "The character name should not contain spaces."
    
#     if type(STR) is not int or type(INT) is not int or type(CHA) is not int:
#         return "All stats should be integers."
    
#     if STR < 1 or INT < 1 or CHA < 1:
#         return "All stats should be no less than 1."
    
#     if STR > 4 or INT > 4 or CHA > 4:
#         return "All stats should be no more than 4."
    
#     if (STR + INT + CHA) != 7:
#         return "The character should start with 7 points."
    
#     result_str = (full_dot * STR) + (empty_dot * (10 - STR))
#     result_int = (full_dot * INT) + (empty_dot *(10 - INT))
#     result_cha = (full_dot * INT) + (empty_dot * (10 - CHA))

#     return f'{name}\nSTR {result_str}\nINT {result_int}\nCHA {result_cha}'
    
    
    
#     # print(f'STR {result_str}')

# print(create_character('red ', 4, 2, 1))
    

# developers = ['Naomi', 'Dario', 'Jessica', 'Tom']
# ids = [1, 2, 3, 4]

# for name, id in zip(developers, ids):
#     print(f'Name: {name}')
#     print(f'ID: {id}')


# numbers = [1, 2, 3, 4, 5]
# even_numbers = filter(lambda x: x % 2 == 0, numbers)  # <filter object at ...>
# print(list(even_numbers))  # [2, 4]

# То, что мы знаем о структуре таблицы
columns = ["user_id", "email", "is_active", "balance"]

# То, что прилетело из голой базы данных
db_rows = [
    (101, "admin@mail.com", True, 5000.50),
    (102, "bot@mail.com", False, 0.0),
    (103, "sergey@mail.com", True, 150.00)
]

# Превращаем сырые кортежи в список словарей для отправки на фронтенд
json_response = []
for row in db_rows:
    # zip склеивает названия колонок с реальными значениями
    user_dict = dict(zip(columns, row))
    json_response.append(user_dict)

# Теперь это валидный формат для отправки по API
print(json_response[0]) 
# {'user_id': 101, 'email': 'admin@mail.com', 'is_active': True, 'balance': 5000.5}
