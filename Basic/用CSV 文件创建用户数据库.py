from IPython.display import clear_output
import csv


def registerUser():
    with open("c:\\Users\\Desktop\\user.csv", mode="a", newline="") as f:
        writer = csv.writer(f, delimiter=",")
        print("To register, please enter your info:")
        email = input("Eamil:")
        password = input("Password:")
        repassword = input("Re-enter password:")
        clear_output()
        if password == repassword:
            writer.writerow([email, password])
            print("Registration successful")
        else:
            print("Passwords do not match")


def loginUser():
    print("To login, please enter your info:")
    email = input("Eamil:")
    password = input("Password:")
    clear_output()
    with open("c:\\Users\\Desktop\\user.csv", mode="r", newline="") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            if row[0] == email and row[1] == password:
                print("Login successful")
                return True
    print("Login failed")
    return False


active = True
logged_in = False
# main loop
while active:
    if logged_in:
        print("1. Logout\n2. Quit")
    else:
        print("1. Register\n2. Login\n3. Quit")
    choice = input("Enter your choice:")
    clear_output()
    if choice == "Register" and logged_in == False:
        registerUser()
    elif choice == "Login" and logged_in == False:
        logged_in = loginUser()
    elif choice == "Logout" and logged_in == True:
        logged_in = False
        print("You are now logged out")
    elif choice == "Quit":
        active = False
        print("Thanks for using our software")
    else:
        print("Invalid choice")
