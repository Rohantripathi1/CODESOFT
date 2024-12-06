#This is self password generator by Rohan Tripathi

import random
import string

def generate_password(length):
    if length < 1:
        return "Password length must be at least 1 character."
    

    characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Choose your password length:"))
        if length <= 0:
            print("Password length must be greater than 0.")
        else:
            password = generate_password(length)
            print(f"Random Password is: {password}")
    except ValueError:
        print("This is not right input! Please enter a numeric value.")

if __name__ == "__main__":
    main()
    
#task 3 Done by Rohan