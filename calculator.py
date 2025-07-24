# Simple Calculator by Ashutosh (CodSoft Internship Project)

def calculator():
    print("\n Welcome to the Calculator5")

    try:
        # Getting inputs from the user
        num1 = float(input("Enter your first number: "))
        num2 = float(input("Enter your second number: "))

        # Showing available operations
        print("\nPick what you wanna do:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")

        choice = input("Enter your choice (1/2/3/4): ")

        # Processing the choice
        if choice == '1':
            output = num1 + num2
            symbol = '+'
        elif choice == '2':
            output = num1 - num2
            symbol = '-'
        elif choice == '3':
            output = num1 * num2
            symbol = '*'
        elif choice == '4':
            if num2 == 0:
                print("\n⚠️ Hold up! Division by zero isn't allowed.")
                return
            output = num1 / num2
            symbol = '/'
        else:
            print("\n❌ Invalid choice. Try 1 to 4.")
            return

        # Final result
        print(f"\n✅ Output: {num1} {symbol} {num2} = {output}")

    except ValueError:
        print("\n❌ Invalid input. Please enter numbers only.")

# Run it
calculator()