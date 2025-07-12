number1 = int(input("Enter the first number"))
number2 = int(input("Enter the second number"))


actions1 = input( "Choose one of the actions you want to apply to your numbers.(- , + , * , /)")

actions=[ '-' , '+' , '*' , '/' ]


if actions1 in actions:
    if actions1 == '-':
        print("Result :", number1 - number2)
    elif actions1 == '+':
        print("Result :", number1 + number2)
    elif actions1 =='*':
        print("Result :", number1 * number2)
    elif actions1 =='/' and number2 != 0:
        print("Result :", number1 / number2)
    else:
        print("Rusult :You can't divide by zero")
else:
    print ("Don't be meanie, choose an action from the list.")