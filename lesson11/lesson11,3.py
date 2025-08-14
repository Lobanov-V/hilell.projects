def is_even(n: int) -> bool:
    return str(abs(n))[-1] in "02468"


assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
assert is_even(24945638940386**3) == True, 'Test3.1'

print("ok")


print(is_even(111))
print(is_even(112))





























# def is_even(n: int) -> bool:
#     return (n & 1) == 0