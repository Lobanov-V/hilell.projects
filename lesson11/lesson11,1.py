def prime_generator(ceiling:int)-> list:
    for num in range(2, ceiling ):
        for divisor in range(2, int (num**0.5)+1):
            if num % divisor == 0:
                break
        else:
            yield num

print(list(prime_generator(100)))