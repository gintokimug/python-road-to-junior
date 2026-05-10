def open_or_senior(data):
    result = []
    for pair in data:
        if int(pair[0]) >= 55 and int(pair[1]) > 7:
                result.append('Senior')
        else:
                result.append('Open')
    return result
            
membership =[[14, 18], [80, 6], [55, 25] ,[48, 50], [32, 2], [54, 18], [65, 25]]  
print(open_or_senior(membership))

def open_or_senior(data):
      return[
    "Senior" if age >= 55 and handicap > 7 else "Open"for age, handicap in data
      ]