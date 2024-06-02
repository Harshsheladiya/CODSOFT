def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "ERROR: Division by zero not possible"

def main():
    while True:
        print("\n Calculator:")
        print("1. addition:")
        print("2. subtraction:")
        print("3. multiplication:")
        print("4. division:")
        print("5. Exit:")

        choice = input("\nEnter your choice:-> ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number:-> "))
            num2 = float(input("Enter second number:-> "))

            if choice == '1':
                print(f"Result:-> {add(num1, num2)}")
            elif choice == '2':
                print(f"Result:-> {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result:-> {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result:-> {divide(num1, num2)}")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please Enter only 1 to 5..")

if __name__ == "__main__":
    main()
