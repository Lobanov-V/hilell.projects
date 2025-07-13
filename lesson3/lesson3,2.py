

my_list = [1,2,3,4,5]
if len(my_list) >= 1:
    x=my_list.pop(-1)
    my_list.insert(0,x)
    print(my_list)
else:print(my_list)


# не работает с пустым
# my_list =[]
# x=my_list.pop(-1)
# my_list.insert(0,x)
# print(my_list)
#
# my_list = [12, 3, 4, 10, 8]
# x=my_list.pop(-1)
# my_list.insert(0,x)
# print(my_list)