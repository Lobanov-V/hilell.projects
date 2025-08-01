def second_index(a:str , b:str) -> int|None:
    first_index = a.find(b)
    if first_index == -1:
        return None

    second_index=a.find(b,first_index+1)
    return second_index


a=input("enter first string")
b=input("enter part of the first string ")

print(second_index(a,b))