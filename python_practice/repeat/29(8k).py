# Задача Каты
# У меня есть кошка и собака.

# Я завела их одновременно, когда они были еще котятами/щенками. Это было humanYears лет назад.

# Узнайте, сколько им сейчас лет, [humanYears,catYears,dogYears]

# ПРИМЕЧАНИЯ:

# humanYears >= 1
# humanYears только целые числа
# Кошачьи Годы
# 15количество лет коту в первый год
# +9количество лет коту во второй год
# +4количество лет коту в каждый последующий год
# Собачьи годы
# 15количество собачьих лет за первый год
# +9количество собачьих лет за второй год
# +5количество собачьих лет за каждый последующий год


def human_years_cat_years_dog_years(human_years):
    catYears = 0
    dogYears = 0

    for years in range(human_years):
        human_years >= 1
        if human_years == 1:
            catYears += 15
            dogYears += 15
            return [human_years,catYears,dogYears]        
        if human_years == 2:
            catYears += 24
            dogYears += 24
            return [human_years,catYears,dogYears]
        elif human_years >= 3:
            catYears += 24 +(4 * (human_years - 2))
            dogYears += 24 +(5 * (example - 2))
            return [human_years,catYears,dogYears]

example = 8

print(human_years_cat_years_dog_years(example))



