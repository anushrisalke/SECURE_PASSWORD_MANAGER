import random
import string

password = {}

# Load saved passwords


def load_password():
 try:
    with open("password.txt", "r") as file:
        for line in file:
            website, pwd = line.strip().split(":")
            password[website] = pwd
 except FileNotFoundError:
    pass

def save_to_file():
    with open("password.txt", "w") as file:
        for website, pwd in password.items():
            file.write(f"{website}:{pwd}\n")

# Function to generate a random password
def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%&*"
    pwd = "".join(random.choice(chars) for _ in range(8))
    return pwd

def view_passwords():
    if not password:
        print("No passwords saved.")
    else:
        print("\nSaved Passwords:")
        for site, pwd in password.items():
            print(site, ":", pwd)

load_password()

while True:
    print("\n----- PERSONAL PASSWORD MANAGER -----")
    print("1. Save Password")
    print("2. View Password")
    print("3. Generate Password")
    print("4. Search Password")
    print("5. Update Password")
    print("6. Delete password")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        site = input("Enter website: ").lower()
        pwd = input("Enter password: ")

        password[site] = pwd

        with open("password.txt", "a") as file:
            file.write(f"{site}:{pwd}\n")

        print("Password saved successfully!")

    elif choice == "2":
        view_passwords()

    elif choice == "3":
        print("Generated Password:", generate_password())

    elif choice == "4":
     site = input("Enter website to search: ").lower()

     if site in password:
        print(f"Website : {site}")
        print(f"Password: {password[site]}")
     else:
        print("Website not found!")
    
    elif choice == "5":
     site = input("Enter website to update: ").lower()

     if site in password:
        new_pwd = input("Enter new password: ")

        password[site] = new_pwd

        save_to_file()

        print("Password updated successfully!")

     else:
        print("Website not found!")
   
    elif choice == "6":
     site = input("Enter website to delete: ").lower()

     if site in password:
        del password[site]

        save_to_file()

        print("Password deleted successfully!")

     else:
        print("Website not found!")

    elif choice == "7":
        print("OK ,BYE... Thank you for using Password Manager!")
        break

    else:
        print("Invalid choice. Please try again.")