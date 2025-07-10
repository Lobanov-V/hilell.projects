number = input("Enter a 4-digit number")

n=int(number)

print(n // 1000)
print((n //100) % 10)
print((n //10) % 10)
print(n % 10)
#
# print ((n // 1000) , ((n //100) % 10) , ((n //10) % 10) , (n % 10))
print ((n % 10) , ((n //10) % 10) , ((n //100) % 10) , (n // 1000) )