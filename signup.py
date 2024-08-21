def ask_email():
    email = input("Enter your email address (xxx@xx.xx): ")
    return email

def ask_name():
    name = input("Enter your username: ")
    return name

def set_password():
    password = input("Enter password for your account: ")
    return password

def sign_up():

    f = open("email.txt", "r") 
    lines = f.readlines()

    fcheck = open("check.txt", "r")
    suffixes = fcheck.read().splitlines()

    while True:
        email = ask_email()
        if len(email) == 0:
            print("You can't keep it blank, please try again.")
            continue
        elif email + "\n" in lines:
            print("You cannot use the same email address to sign up for two or more accounts, please try again.")
            continue 
        elif any(email.endswith(suffix) for suffix in suffixes):
            break
        else:
            print("Please enter a proper email address, please try again.")
            continue


    while True:
        name = ask_name()
        if len(name) == 0:
            print("Your name should not be blank, please try again.")
            continue
        else:
            break

    while True:
        password = set_password()
        if len(password) < 8:
            print("Your password should not be less than 8 characters, please try again.")
        elif len(password) > 8:
            print("Your password should not be more than 8 characters, please try again.")
        else:
            break

    f = open("email.txt", "a")
    f.write(f'{email}\n')
    f.close()

    fname = open("name.txt", "a") 
    fname.write(f'{name}\n')
    fname.close()

    fpass = open("password.txt", "a") 
    fpass.write(f'{password}\n')
    fpass.close()

    print("Success")

sign_up()
