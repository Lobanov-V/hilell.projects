
lst_numbers=[6]

new_list =(lst_numbers[0::2])
if not lst_numbers:
    result = 0
else :
    result=sum(new_list) * lst_numbers[-1]
print(result)


# [1, 3, 5] => 30
# [6] => 36
# [] => 0


