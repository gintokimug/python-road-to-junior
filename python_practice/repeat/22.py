class Fighter(object):
    def __init__(self, name, health, damage_per_attack):
        self.name = name
        self.health = health
        self.damage_per_attack = damage_per_attack



def declare_winner(fighter1, fighter2, first_attacker):
    # 1. Сначала поймем, кто есть кто в первом раунде
    if fighter1.name == first_attacker:
        attacker = fighter1
        defender = fighter2
    else:
        attacker = fighter2
        defender = fighter1

    # 2. Драка до победного конца
    while True:
        # Атакующий бьет защищающегося
        defender.health -= attacker.damage_per_attack
        
        # Проверяем, выжил ли защищающийся
        if defender.health <= 0:
            return attacker.name # Бой окончен, возвращаем имя чемпиона
        
        # 3. Меняемся ролями (тот кто бил, теперь защищается, и наоборот)
        attacker, defender = defender, attacker
    