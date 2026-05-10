def nb_year(p0, percent, aug, p):
    year = 0
    while p0 < p:
        p0 = int(p0 + p0 * (percent/100) + aug)
        year += 1
    return year



p0 = 1000
p = 5000
percent = 0.02
aug = 50
print(nb_year(1000, 0.02, 50, 1200)) 