def goals(laLiga, copaDelRey, championsLeague):

    return int(laLiga + copaDelRey + championsLeague)

laLiga = 5
copaDelRey = 7
championsLeague = 8
print(goals(laLiga, copaDelRey, championsLeague))

def goals(*a):
    return sum(a)