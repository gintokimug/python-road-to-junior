def is_pangram(st):
    # результат for элемент in источник if условие
    # if all(item in check_list for item in my_list):
    # Метод .isalpha() проверяет, является ли символ буквой


    # alphabet = "abcdefghijklmnopqrstuvwxyz"
    # st = set(st)
    # if all(char in st for char in alphabet):
    #         return True
    # else:
    #         return False
        
def is_pangram(st):        
     st = str(st).lower()
     alphabet = "abcdefghijklmnopqrstuvwxyz"
     letters_only = {char for char in st.lower() if char in alphabet}
     return len(letters_only) == 26

def is_pangram(st):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letters_only = [char for char in st.lower() if char in alphabet]
    return len(letters_only) == 26



example_1 =  ["The quick brown fox jumps over the lazy dog.",
"Cwm fjord bank glyphs vext quiz",
"Pack my box with five dozen liquor jugs.",
"How quickly daft jumping zebras vex.",
"ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ" ]

example_2 = "abcdefghijklmnopqrstuvwxyz"
print(is_pangram({example_2}))
    