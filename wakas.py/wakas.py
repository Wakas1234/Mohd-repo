def get_user_input():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")

    # Basic input validation
    if not name or not age or not email:
        print("Please fill out all fields.")
        return get_user_input()

    try:
        age = int(age)
        if age < 18:
            print("You must be 18 or older to register.")
            return get_user_input()
    except ValueError:
        print("Invalid age. Please enter a valid number.")
        return get_user_input()

    return name, age, email

def main():
    print("Welcome to the registration form.")
    name, age, email = get_user_input()
    print("\nRegistration successful!")
    print("Name: {}\nAge: {}\nEmail: {}".format(name, age, email))

if __name__ == '__main__':
   main()