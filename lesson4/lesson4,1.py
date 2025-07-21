lst_numbers=[]

zero_count=lst_numbers.count(0)

for x in range(zero_count):
    lst_numbers.remove(0)

for x in range(zero_count):
    lst_numbers.append(0)

print(lst_numbers)










# lst_numbers=[9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
#
# zero_count=0
# zero_list=[]
#
# for x in lst_numbers:
#     if x==0:
#         zero_count+=1
#     else:
#         zero_list.append(x)
#
# for _ in range(zero_count):
#     zero_list.append(0)
#
# print(zero_list)

# [0, 1, 0, 12, 3] -> [1, 12, 3, 0, 0]
# [0] -> [0]
# [1, 0, 13, 0, 0, 0, 5] -> [1, 13, 5, 0, 0, 0, 0]
# [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0] -> [9, 7, 31, 45, 45, 45, 96, 0, 0, 0, 0, 0, 0, 0]


