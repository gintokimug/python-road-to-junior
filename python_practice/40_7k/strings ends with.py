# Дополните решение так, чтобы оно возвращало true, если первый аргумент (строка), переданный в функцию, заканчивается вторым аргументом (тоже строкой).

# Примеры:

# Inputs: "abc", "bc"
# Output: true

# Inputs: "abc", "d"
# Output: false

# def solution(text, ending):
#     # your code here...
#     while text[-len(ending)] == ending:
#         return True 
#     else:
#         return False
    
# input = ("samurai", "ai")

# print(solution("samurai", "ai"))

def solution(text, ending):
    return text[-len(ending):] == ending
