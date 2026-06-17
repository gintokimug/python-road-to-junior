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

# # То, что мы знаем о структуре таблицы
# columns = ["user_id", "email", "is_active", "balance"]

# # То, что прилетело из голой базы данных
# db_rows = [
#     (101, "admin@mail.com", True, 5000.50),
#     (102, "bot@mail.com", False, 0.0),
#     (103, "sergey@mail.com", True, 150.00)
# ]

# # Превращаем сырые кортежи в список словарей для отправки на фронтенд
# json_response = []
# for row in db_rows:
#     # zip склеивает названия колонок с реальными значениями
#     user_dict = dict(zip(columns, row))
#     json_response.append(user_dict)

# # Теперь это валидный формат для отправки по API
# print(json_response[0]) 
# # {'user_id': 101, 'email': 'admin@mail.com', 'is_active': True, 'balance': 5000.5}










# import re

# medical_records = [
#     {
#         'patient_id': 'P1001',
#         'age': 34,
#         'gender': 'Female',
#         'diagnosis': 'Hypertension',
#         'medications': ['Lisinopril'],
#         'last_visit_id': 'V2301',
#     },
#     {
#         'patient_id': 'p1002',
#         'age': 47,
#         'gender': 'male',
#         'diagnosis': 'Type 2 Diabetes',
#         'medications': ['Metformin', 'Insulin'],
#         'last_visit_id': 'v2302',
#     },
#     {
#         'patient_id': 'P1003',
#         'age': 29,
#         'gender': 'female',
#         'diagnosis': 'Asthma',
#         'medications': ['Albuterol'],
#         'last_visit_id': 'v2303',
#     },
#     {
#         'patient_id': 'p1004',
#         'age': 56,
#         'gender': 'Male',
#         'diagnosis': 'Chronic Back Pain',
#         'medications': ['Ibuprofen', 'Physical Therapy'],
#         'last_visit_id': 'V2304',
#     }
# ]

# def find_invalid_records(
#     patient_id, age, gender, diagnosis, medications, last_visit_id
# ):
#     constraints = {
#         'patient_id': isinstance(patient_id, str)
#         and re.fullmatch('p\d+', patient_id, re.IGNORECASE),
#         'age': isinstance(age, int) and age >= 18,
#         'gender': isinstance(gender, str) and gender.lower() in ('male', 'female'),
#         'diagnosis': isinstance(diagnosis, str) or diagnosis is None,
#         'medications': isinstance(medications, list)
#         and all([isinstance(i, str) for i in medications]),
#         'last_visit_id': isinstance(last_visit_id, str)
#         and re.fullmatch('v\d+', last_visit_id, re.IGNORECASE)
#     }
#     return [key for key, value in constraints.items() if not value]

# def validate(data):
#     is_sequence = isinstance(data, (list, tuple))

#     if not is_sequence:
#         print('Invalid format: expected a list or tuple.')
#         return False
        
#     is_invalid = False
#     key_set = set(
#         ['patient_id', 'age', 'gender', 'diagnosis', 'medications', 'last_visit_id']
#     )

#     for index, dictionary in enumerate(data):
#         if not isinstance(dictionary, dict):
#             print(f'Invalid format: expected a dictionary at position {index}.')
#             is_invalid = True
#             continue

#         if set(dictionary.keys()) != key_set:
#             print(
#                 f'Invalid format: {dictionary} at position {index} has missing and/or invalid keys.'
#             )
#             is_invalid = True
#             continue

#         invalid_records = find_invalid_records(**dictionary)
        

#     if is_invalid:
#         return False
#     print('Valid format.')
#     return True

# validate(medical_records)











    # dict_sett = {
    #     'SofiA' : 'Main',
    #     'ALOSHA' : 'MAIN',
    #     'Sergey' : 'Main'
    #             }
    
    # tuple_kv = (('KEY' , 'ONE' ), ('Key', 'Two'), ('keY', 'threE'))




test_settings = { 
                'THEME' : 'LIGHT'
                }


def add_setting(dict_sett, tuple_kv):

    lowercase_dict = {key.lower() : value.lower() for key,value in dict_sett.items()}

    new_key = tuple_kv[0].lower()
    new_value = tuple_kv[1].lower()

    if new_key in lowercase_dict:
        return f"Setting '{new_key}' already exists! Cannot add a new setting with this name."
    
    dict_sett[new_key] = new_value
    return f"Setting '{new_key}' added with value '{new_value}' successfully!"
    

def update_setting(dict_sett, tuple_kv):

    lowercase_dict = {key.lower() : value.lower() for key,value in dict_sett.items()}
    
    new_key = tuple_kv[0].lower()
    new_value = tuple_kv[1].lower()

    if new_key not in lowercase_dict:
        return f"Setting '{new_key}' does not exist! Cannot update a non-existing setting."

    
    dict_sett[new_key] = new_value
    return f"Setting '{new_key}' updated to '{new_value}' successfully!"



def delete_setting(dict_sett, tuple_kv):

    low_key = tuple_kv.lower()

    if low_key in dict_sett:
        del dict_sett[low_key]
        return f"Setting '{low_key}' deleted successfully!"
    
    if not low_key in dict_sett:
        return f"Setting not found!"


def view_settings(dict_sett):
    # 1. Если словарь пуст - возвращаем базовую фразу
    if not dict_sett:
        return "No settings available."
    
    # 2. Добавляем тот самый скрытый заголовок, который просит платформа!
    result = "Current User Settings:\n"
    
    # 3. Перебираем настройки
    for key, value in dict_sett.items():
        # Пишем ключ с большой буквы (capitalize), двоеточие, значение и перенос строки \n
        result += f"{key.capitalize()}: {value}\n"
        
    return result

    

       
    
    

    

    

print(update_setting({'theme': 'light'}, ('volume', 'high')))



    
    
