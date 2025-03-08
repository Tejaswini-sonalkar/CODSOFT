def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def display_menu():
    print("\nSimple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

def main():
    while True:
        display_menu()
        
        try:
            
            choice = input("Enter the operation number (1/2/3/4) or 'q' to quit: ")
            
            if choice == 'q':
                print("Goodbye!")
                break
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            if choice == '1':
                result = add(num1, num2)
                print(f"Result: {num1} + {num2} = {result}")
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"Result: {num1} - {num2} = {result}")
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"Result: {num1} * {num2} = {result}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"Result: {num1} / {num2} = {result}")
            else:
                print("Invalid choice! Please select a valid operation.")
        except ValueError:
            print("Invalid input! Please enter numerical values.")
        except Exception as e:
            print(f"Error: {e}")
if __name__ == "__main__":
    main()

