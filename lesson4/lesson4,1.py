lst_numbers=[1,3,2,0,5,3,0,8,0]

zero_count=0
zero_list=[]

for x in lst_numbers:
    if x==0:
        zero_count+=1
    else:
        zero_list.append(x)

for _ in range(zero_count):
    zero_list.append(0)

print(zero_list)

