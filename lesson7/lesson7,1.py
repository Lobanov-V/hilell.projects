def say_hi(name:str, age:int) -> str:
    return f"Hi. My name is {name} and I'm {age} years old"

usser_name=input('Enter your name: ')
usser_age=int(input('Enter your age: '))

print(say_hi(usser_name,usser_age))



assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
print('ОК')