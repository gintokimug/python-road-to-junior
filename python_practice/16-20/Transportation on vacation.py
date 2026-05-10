def rental_car_cost(d):
    for day in range(d):
        day = 40
        arenda = day * d
        if d >= 7:
            arenda -= 50
        elif d > 3 < 7:
            arenda -= 20
        return arenda 

example = 7
print(rental_car_cost(example))
