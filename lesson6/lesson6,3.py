while True:
    user_number =input("Enter an integer (or 'exit' to quit): ")

    if user_number == 'exit':
        print("Goodbye")
        break

    if not user_number.lstrip('-').isdigit():
        print("Please enter a valid integer.")
        continue

    user_number=abs(int(user_number))

    while user_number > 9 :
        outcome = 1
        for digit in str(user_number):
            outcome *= int(digit)
        user_number = outcome

    print(f"Result: {user_number}")