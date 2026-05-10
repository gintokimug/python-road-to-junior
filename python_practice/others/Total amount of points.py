def points(games):
    total_points = 0
    for point in games:
        parts = point.split(':')
        if int(parts[0]) > int(parts[1]):
            total_points += 3
        if int(parts[0]) == int(parts[1]):
            total_points += 1
    return total_points  
score = ['3:2','4:0','0:3','2:2','2:1','3:4','1:3','3:3','3:1','4:3']
print(points(score))
            

        
    


