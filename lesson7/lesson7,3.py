def second_index(a:str , b:str) -> int|None:
    first_index = a.find(b)
    if first_index == -1:
        return None

    second_index=a.find(b,first_index+1)
    return second_index


a=input("enter first string")
b=input("enter part of the first string ")

print(second_index(a,b))

assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')