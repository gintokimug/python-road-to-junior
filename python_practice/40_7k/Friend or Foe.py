# Напишите программу, которая фильтрует список строк и возвращает список, в котором будут только имена ваших друзей.

# Если в имени ровно 4 буквы, можете быть уверены, что это ваш друг! В противном случае можете быть уверены, что это не он...

# Input = ["Ryan", "Kieran", "Jason", "Yous"]
# Output = ["Ryan", "Yous"]

# Input = ["Peter", "Stephen", "Joe"]
# Output = []
# Входные строки будут содержать только буквы.
# Примечание: сохраните исходный порядок имен в выводе.

def friend(x):
    #Code
    friends_list = []

    for name in x:
        if len(name) == 4:
            friends_list.append(name)
    return friends_list


input = ["Ryan", "Kieran", "Jason", "Yous"]

print(friend(input))