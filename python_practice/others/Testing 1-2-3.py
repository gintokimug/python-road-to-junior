def number(lines):
    result = []
    count = 1
    for letter in lines:
        formated_lines = f'{count} : {letter}'
        result.append(formated_lines)
        count += 1
    return result

lines = (["a", "b", "c"])
print(number(lines))



def list_of_names(names):
    return [f"Привет, {name}!" for name in names]

names = ["Иван", "Анна"]
print(list_of_names(names))
  








