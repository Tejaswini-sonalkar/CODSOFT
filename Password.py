import random
import string

def generate_password(length, complexity=4):

    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    
    if complexity == 1:
        characters = lower_case
    elif complexity == 2:
        characters = lower_case + upper_case
    elif complexity == 3:
        characters = lower_case + upper_case + digits
    elif complexity == 4:
        characters = lower_case + upper_case + digits + special_characters
    else:
        raise ValueError("Complexity level must be between 1 and 4.")
    
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def main():
    print("Welcome to the Password Generator!")
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length < 6:
                print("Password length should be at least 6 characters for better security.")
                continue
            break
        except ValueError:
            print("Please enter a valid number for the length.")

    while True:
        try:
            complexity = int(input("Enter the complexity level (1: Lowercase, 2: Lower + Uppercase, 3: Lower + Upper + Digits, 4: Lower + Upper + Digits + Special Characters): "))
            if complexity not in [1, 2, 3, 4]:
                print("Please choose a complexity level between 1 and 4.")
                continue
            break
        except ValueError:
            print("Please enter a valid number for the complexity level.")
                           
    
    password = generate_password(length, complexity)
    print(f"\nYour generated password is: {password}")
if __name__ == "__main__":
    main()
