my_list=[1, 2, 3, 4, 5]

my_list2=my_list[1::2]

new_list1=[x for x in my_list if x not in my_list2]
# print(new_list1)

combi_list = [new_list1 , my_list2 ]
print(combi_list)


# [1, 2, 3, 4, 5, 6] => [[1, 2, 3], [4, 5, 6]]
# [1, 2, 3] => [[1, 2], [3]]
# [1, 2, 3, 4, 5] => [[1, 2, 3], [4, 5]]
# [1] => [[1], []]
# [] => [[], []]
