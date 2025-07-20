while True :
    print("Select an operation: ")
    print("1.Addition (+)")
    print("2.Subtraction (-)")
    print("3.Multiplication (*)")
    print("4.Division (/)")
    print("5.Exit")

    choice=int(input("Enter your choice: "))


    if choice == 5:
        print("Exit")
        break

    if choice not in [1,2,3,4,5]:
        print("Invalid choice")
        continue

    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    if choice == 1:
        print(a + b)
    elif choice == 2:
        print(a - b)
    elif choice == 3:
        print(a * b)
    elif choice == 4 and b!=0:
        print(a / b)
    else:
        print("Rusult :You can't divide by zero")





 # choice=int(input("Enter your choice: "))