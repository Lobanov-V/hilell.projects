import keyword

your_name = input("Enter your name: ")

valid = True

if not your_name:
    valid = False

elif your_name[0].isdigit():
    valid = False

elif your_name in keyword.kwlist:
    valid = False

elif set(your_name) == {'_'} and len(your_name) > 1:
    valid = False

else:
    for x in your_name:
        if not (x.islower() or x.isdigit() or x == '_'):
            valid = False
            break


print(valid)

# _ => True
# __ => False
# ___ => False
# x => True
# get_value => True
# get value => False
# get!value => False
# some_super_puper_value => True
# Get_value => False
# get_Value => False
# getValue => False
# 3m => False
# m3 => True
# assert => False
# assert_exception => True




















# import string
# import keyword
#
# your_name = input("Enter your name: ")
#
# underscore_count=0
#
# valid=True
# if not your_name:
#     valid = False
#
# elif your_name[0].isdigit():
#     valid=False
#
# elif your_name in keyword.kwlist:
#     valid=False
#
# else:
#     for x in your_name:
#         if x == '_':
#             underscore_count +=1
#
#         elif x.isupper():
#             valid=False
#             break
#         elif x.isspace():
#             valid=False
#             break
#         elif x in string.punctuation and x !='_':
#             valid=False
#             break
#         elif not x.isalnum() and x !='_':
#             valid=False
#             break
#
# if underscore_count > 5:
#     valid=False
#
# print(valid)





