import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    while True:
        print("\nPassword Generator:")
        try:
            length = int(input("Enter desired password length:-> "))
            if length <= 0:
                print("Invalid Please enter only positive number.")
                continue
        except ValueError:
            print("Invalid  Please enter only a number.")
            continue
        
        password = generate_password(length)
        print(f"Generated Password:-> {password}")

        choice = input("Generate another password ?? :-> ")
        if choice.lower() not in ['yes', 'y']:
            break

if __name__ == "__main__":
    main()
