import string
import keyword

your_name = input("Enter your name: ")

underscore_count=0

valid=True

if your_name[0].isdigit():
    valid=False

if your_name in keyword.kwlist:
    valid=False

else:
    for x in your_name:
        if x == '_':
            underscore_count = 0

        elif x.isupper():
            valid=False
            break
        elif x.isspace():
            valid=False
            break
        elif x in string.punctuation and x !='_':
            valid=False
            break
        elif not x in x.isalnum() and x !='_':
            valid=False
            break

if underscore_count > 1:
    valid=False

print(valid)


