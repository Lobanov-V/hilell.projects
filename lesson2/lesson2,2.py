
number = input("Enter a 5-digit number")

n=int(number)

# print(n // 1000)
# print((n //100) % 10)
# print((n //10) % 10)
# print(n % 10)

# print ((n // 1000) , ((n //100) % 10) , ((n //10) % 10) , (n % 10))
# print ((n % 10) , ((n //10) % 10) , ((n //100) % 10) , ((n //1000) % 10) , (n // 10000) )

n1 = n % 10
n2 = (n //10) % 10
n3 = (n //100) % 10
n4 = (n //1000) % 10
n5 = n //10000

reverse = n1 * 10000 + n2 * 1000 + n3 * 100 + n4 * 10 + n5

print(reverse)