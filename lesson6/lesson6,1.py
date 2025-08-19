import string

user_letters=input("Enter two letter")

first , second =user_letters.split("-")

all_letters = string.ascii_letters

first_index = all_letters.index(first)
second_index = all_letters.index(second)

result= all_letters[first_index:second_index +1]
print(result)

