data = [" иван", "Пётр ", " иван ", "АЛЕСКЕЙ", "ПётР"]
clean_names = []
for name in data:
    new_names = name.strip().capitalize()
    clean_names.append(new_names)
unique_names = list(set(clean_names))
final_names = sorted(unique_names)
print(final_names)


        
    


