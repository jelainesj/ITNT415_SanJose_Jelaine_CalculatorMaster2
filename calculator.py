def add(a, b):
    return a + b


def get_number(prompt):
    while True:
        value = input(prompt).strip()
        try:
            return float(value)
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def show_menu():
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Jel's Calculator")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("A - Addition")
    print("S - Subtraction")
    print("M - Multiplication")
    print("D - Division")
    print("X - Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose operation: ").strip().upper()

        if choice == "X":
            print("Thank you for using Jelaine's Calculator Master.")
            break

        if choice not in {"A", "S", "M", "D"}:
            print("Invalid option. Please choose A, S, M, D, or X.")
            continue

        if choice == "A":
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")
            result = add(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")
        else:
            print("This operation is not implemented yet.")


if __name__ == "__main__":
    main()
