# Правила игры «Камень, ножницы, бумага»:

# Камень побеждает ножницы,
# Ножницы побеждают бумагу,
# Бумага побеждает камень,
# Два одинаковых хода — ничья.
# Давайте сыграем!  Вам будут предложены возможные ходы двух игроков в «Камень, ножницы, бумага», и вы должны будете определить, кто из них победил: 
# "Player 1 won!" для игрока 1 и "Player 2 won!" для игрока 2. В случае ничьей верните Draw!.

# Примеры:
# "scissors",     "paper"     --> "Player 1 won!"
# "scissors",     "rock"      --> "Player 2 won!"
# "paper",        "paper"     --> "Draw!"

def rps(p1, p2):
    if "scissors" and "paper":
        return  "Player 1 won!"
    elif "paper" and "rock":
        return "Player 1 won!"
    elif "rock" and "scissors":
        return "Player 1 won!"
    if "scissors" and "paper":
        return  "Player 2 won!"
    elif "paper" and "rock":
        return "Player 2 won!"
    elif "rock" and "scissors":
        return "Player 2 won!"
        return "Draw!"
    elif "scissors" and "scissors":
        return "Draw!"
    elif "rock" and "rock":
        return "Draw!"
    elif "paper" and "paper":
        return "Draw!"