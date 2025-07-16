import random

lst1 = random.randint(3, 10)
random_lst = [random.randint(3, 10) for i in range(lst1)]
print(random_lst)

new_lst=(random_lst[0],random_lst[2],random_lst[-2])
print(new_lst)





















# print(list_numbers.count(0))
# # показывает сколько раз эелемент встречаеться в списке
# print(list_numbers.index(0,1))
# # показывает сколько раз после выбраного элемента тот встречаеться в списке
# print(list_numbers.sort())
# print(list_numbers)
# # сортирует список но не возвразает так что нужно использовать в две строки
# print(max(list_numbers))
# print(min(list_numbers))
#
# print(all(list_numbers))
# # если все элементы в списке имеют значение тру то и функция вернет нам тру
# print(any(list_numbers))
# # если хотя бы один элемент из списка тру вернет нам значение тру
# from copy import deepcopy
# list_numbers2=deepcopy(list_numbers)
# # копирование списка с его клонированием что дает возможность менять их независимо друг от друга