def get_input(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Invalid input! Please enter numeric values only.")
        return None

def divide():
    a = get_input("Enter numerator: ")
    b = get_input("Enter denominator: ")
    if a is None or b is None or b == 0:
        print("Error: Division by zero is not allowed." if b == 0 else "")
        return None
    return a / b

def exponentiate():
    a = get_input("Enter base: ")
    b = get_input("Enter exponent: ")
    return a ** b if a is not None and b is not None else None

def remainder():
    a = get_input("Enter dividend: ")
    b = get_input("Enter divisor: ")
    if a is None or b is None or b == 0:
        print("Error: Division by zero is not allowed." if b == 0 else "")
        return None
    return a % b

def summation():
    a = get_input("Enter starting number: ")
    b = get_input("Enter ending number: ")
    if a is None or b is None or a > b:
        print("Error: The second number must be greater than the first number." if a > b else "")
        return None
    return sum(range(a, b + 1))

def main():
    operations = {'D': divide, 'E': exponentiate, 'R': remainder, 'F': summation}
    while True:
        print("\n=== Math Operations Menu ===\n[D] - Divide\n[E] - Exponentiation\n[R] - Remainder\n[F] - Summation\n[Q] - Quit")
        choice = input("Enter your choice: ").strip().upper()
        if choice == 'Q':
            print("Thank you for using the program. Goodbye!")
            break
        result = operations.get(choice, lambda: print("Invalid choice! Please select a valid option from the menu."))()
        if result is not None:
            print("Result:", result)
        if input("Do you want to perform another operation? (Y/N): ").strip().upper() != 'Y':
            print("Exiting program. Have a great day!")
            break

if __name__ == "__main__":
    main()
