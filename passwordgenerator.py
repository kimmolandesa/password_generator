import random
import string

def get_password_length():
    while True:
        try:
            length = int(input("Welcome to the password generator. How many characters long should your password be?: "))
            if length < 1:
                print("Password length must be a positive integer.")
                continue
            return length
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def get_password_chars():
    password_chars = ''
    while True:
        print("Please choose the type of characters to include in your password:")
        print("1. Digits")
        print("2. Letters")
        print("3. Punctuation")
        print("4. All")
        print("5. Done")
        try:
            password_type = int(input("Enter your choice: "))
            if password_type == 1:
                password_chars += string.digits
            elif password_type == 2:
                password_chars += string.ascii_letters
            elif password_type == 3:
                password_chars += string.punctuation
            elif password_type == 4:
                password_chars += string.digits + string.ascii_letters + string.punctuation
                break
            elif password_type == 5:
                break
            else:
                print("Invalid option. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    return password_chars

def generate_password(length, chars):
    password = [random.choice(chars) for _ in range(length)]
    return ''.join(password)

def save_password(password):
    while True:
        save = input("Would you like to save the password in a file? Y/n: ")
        if save.lower() == "y":
            try:
                with open("password.txt", "a") as f:
                    f.write(password + "\n")
                print("Password saved to password.txt")
                break
            except IOError:
                print("Unable to write to file.")
                break
        elif save.lower() == "n":
            break
        else:
            print("Invalid input. Please enter Y or n.")

def restart_program():
    while True:
        restart = input("Would you like to generate another password? Y/n: ")
        if restart.lower() == "y":
            main()
            break
        elif restart.lower() == "n":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please enter Y or n.")

def password_strength_check(password):
    strength = 0
    if len(password) < 8:
        print("Password is too short. It should be at least 8 characters.")
    elif len(password) >= 12:
        strength += 3
    else:
        strength += 1

    if (any(c.islower() for c in password) 
        and any(c.isupper() for c in password) 
        and any(c.isdigit() for c in password) 
        and any(c in string.punctuation for c in password)):
        strength += 3
    elif (any(c.islower() for c in password) 
          and any(c.isupper() for c in password) 
          and any(c.isdigit() for c in password)):
        strength += 2
    elif (any(c.islower() for c in password) 
          and any(c.isupper() for c in password) 
          and any(c in string.punctuation for c in password)):
        strength += 2
    elif (any(c.islower() for c in password) 
          and any(c.isdigit() for c in password) 
          and any(c in string.punctuation for c in password)):
        strength += 2
    elif (any(c.isupper() for c in password) 
          and any(c.isdigit() for c in password) 
          and any(c in string.punctuation for c in password)):
        strength += 2
    elif "abc" or "123" in password:
        strength-=1
    else:
        print("Password is too weak. It should contain at least three types of characters.")

    if strength == 6:
        print("Password strength: Strong")
    elif strength == 4:
        print("Password strength: Medium")
    else:
        print("Password strength: Weak")

def test_your_own_password():
    yourpassword= input("What's your password?: ")
    password_strength_check(yourpassword)
    
def startpage():
    print("Welcome to the Password Strength Checker! \n")
    print("This program will help you determine the strength of your password. \n")
    print("This app also generates passwords for your own use")
    print("Let's proceed. Do you want to (1) generate a password or (2) check if your password is strong enough?")
    choice_made= int(input("Enter your choice: "))
    if choice_made == 1:
        length = get_password_length()
        chars = get_password_chars()
        password = generate_password(length, chars)
        print("Generated password:", password)
        password_strength_check(password)
        save_password(password)
        restart_program()
        password_strength_check()
    elif choice_made == 2:
        test_your_own_password()
        restart_program()

    
def main():
    startpage()


if __name__ == "__main__":
    main()