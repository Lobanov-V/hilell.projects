def say_hi(name:str, age:int) -> str:
    return f"Hi. My name is {name} and I'm {age} years old"

usser_name=input('Enter your name: ')
usser_age=int(input('Enter your age: '))

print(say_hi(usser_name,usser_age))