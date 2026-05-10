# В этом задании вам нужно создать функцию, которая принимает список неотрицательных целых чисел и строк и возвращает новый список, в котором строки отфильтрованы.

# Пример
# filter_list([1,2,'a','b']) == [1,2]
# filter_list([1,'a','b',0,15]) == [1,0,15]
# filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

# def filter_list(l):
#     new_list = []
#     for element in l:
#         if element == int:
#             new_list += element
#         else:
#             element = ''

# def filter_list(l):
#     flist = list(l)
#     new_list = []
#     for element in l:
#         if element == str:
#             flist.pop(element)
#         else:
#            new_list += element 


def filter_list(l):
    new_list = []
    for element in l:
        if type(element) is int:
            new_list.append(element)
    return new_list


def filter_list(l):
    return [x for x in l if isinstance(x, int)]
        

example = [1,'a','b',0,15]
print(filter_list(example))




# Постянно ошибаюсь на NOne, определлить для себя раз и навсегда почему так происходит .
#  НЕ делать +=  , когда это можно легко заменить append , гораздо практичнее и красивее 
#  проверял элемент через == int ,  ещё одна глупость, всегда выдаст False, подобное необходимо делать через type(element) is int/str/ etc
#  Ещё Ишка показала новую функцию  isinstance (объект, тип) проверять нужного ли типа данные на входе, выходе 