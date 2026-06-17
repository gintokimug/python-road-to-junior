"""
В архиве лежит важный артефакт. Пароль от него зашифрован в потоке проклятой энергии. Твоя задача — написать парсер, который расшифрует этот поток по правилам Магической Битвы.

Изначально твой уровень проклятой энергии равен 0.
Парсер принимает на вход строку и читает её по одному символу. Каждая команда меняет твой уровень энергии:

p (Punch): Удар проклятой энергией. Увеличивает энергию на 5.

r (Reverse Cursed Technique): Обратная проклятая техника. Лечит и прибавляет 10.

d (Damage): Получение урона. Отнимает 3. (Важно: энергия не может опуститься ниже нуля. Если после урона энергия уходит в минус, она становится равной 0).

b (Black Flash): Черная молния. Умножает текущую энергию на 2.

e (Domain Expansion): Расширение территории. Добавляет текущее значение энергии в итоговый массив результатов.

Любые другие символы (буквы, цифры, знаки препинания) — это проклятия низшего уровня, парсер должен их просто игнорировать.

Твой инпут (Payload):
"p_p_b_e_!!!_r_d_b_e_???_p_r_b_b_e_x_d_d_d_d_e"
"""

# def solution(Payload : str):
#     energy : int = 0
#     result = []

#     for move in Payload:

#         if move == 'p':
#             energy += 5
#         elif move == 'r':
#             energy += 10
#         elif move == 'd':
#             energy -= 3
#         elif move == 'b':
#             energy *= 2
#         elif move == 'e':
#             result.append(energy)
#     return result

# example = "p_p_b_e_!!!_r_d_b_e_???_p_r_b_b_e_x_d_d_d_d_e"
# print(solution(example))


# def quick_sort(arr):
# 	if len(arr) <= 1:
# 	    return arr
	
# 	# выбираем опорный элемент Pivot
# 	# Можно брать любой, для надёжности берётся из середины
# 	pivot = arr[len(arr) // 2]
	
# 	# Разделение - линейная работа О(n)
# 	# Проход по списку и раскидка элементов
# 	left = [x for x in arr if x < pivot]
# 	middle = [x for x in arr if x == pivot]
# 	right = [x for x in arr if x > pivot]
	
# 	# Рекурсия и склейка 
# 	# функция сортирует элементы и складывает 
# 	return quick_sort(left) + middle + quick_sort(right)
# print(quick_sort([5, 2, 9, 1, 5, 6]))



# def valid(example: str) -> bool:
    
#     stack = []
    
#     for char in example:
        
#         if char == "(" or char == '{' or char == '[':
#             stack.append(char)
    
#         print(stack)
    
#         if char == ")":
#             if len(stack) == 0:
#                 return False
            
#             if stack[-1] != '(':
#                 return False
#             else:
#                 stack.pop()
            
#         if char == "}":
#             if len(stack) == 0:
#                 return False
            
#             if stack[-1] != '{':
#                 return False
#             else:
#                 stack.pop()
            
#         if char == "]":
#             if len(stack) == 0:
#                 return False
            
#             if stack[-1] != '[':
#                 return False
#             else:
#                 stack.pop()
                
                
# #     return True



# def shame(bracket : str):
#     dist_bracket = {')' : '('} , {'}' : '{'}, {'[' : ']'}
#     print (dist_bracket[0])
  


    
# test = ("{{}}[()]")
# print(test) 

# def pin_extractor(poems):
#     secret_codes = []
#     for poem in poems:
#         secret_code = ''
#         lines = poem.split('\n')
#         for line_index, line in enumerate(lines):
#             words = line.split()
#             if len(words) > line_index:
#                 secret_code += str(len(words[line_index]))
#             else:
#                 secret_code += '0'
#         secret_codes.append(secret_code)
#     return secret_codes
        

# poem = """Stars and the moon
# shine in the sky
# white and
# until the end of the night"""

# poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
# poem3 = 'There\nonce\nwas\na\ndragon'

# print(pin_extractor([poem, poem2, poem3]))

# def number_pattern(n: int):
#         if n < 0:
#              return 'Argument must be an integer greater than 0.'
#         if n % 1 != 0:
#             return 'Argument must be an integer value.'
     
#         return ' '.join(str(num) for num in range(1, n + 1))


# n = 4
# print((number_pattern(n )))


import re

medical_records = [
    {
        'patient_id': 'P1001',
        'age': 34,
        'gender': 'Female',
        'diagnosis': 'Hypertension',
        'medications': ['Lisinopril'],
        'last_visit_id': 'V2301',
    },
    {
        'patient_id': 'p1002',
        'age': 47,
        'gender': 'male',
        'diagnosis': 'Type 2 Diabetes',
        'medications': ['Metformin', 'Insulin'],
        'last_visit_id': 'v2302',
    },
    {
        'patient_id': 'P1003',
        'age': 29,
        'gender': 'female',
        'diagnosis': 'Asthma',
        'medications': ['Albuterol'],
        'last_visit_id': 'v2303',
    },
    {
        'patient_id': 'p1004',
        'age': 56,
        'gender': 'Male',
        'diagnosis': 'Chronic Back Pain',
        'medications': ['Ibuprofen', 'Physical Therapy'],
        'last_visit_id': 'V2304',
    }
]

