data = {  # Database
    "Mahesh": "ghghghhg",  # Keys are username and corresponding values are password
    "Shilpa": "dfdfdffd",
    "Phoenix": "cvcvcvvc",
    "Pegasus": "23sd23sd"
}

operation = int(input("For login press 1 and for signing in press 2 :"))  # Logging in or Signing in checker
if operation == 1:
    pass_flag = 3
    username = input("Enter your user name :")
    while True:
        if username not in data:  # if username is not found in the database then..
            print("Username not Found")
            username = input("Enter your user name :")
        else:
            break
    password = input("Enter your password :")
    while pass_flag != 0:  # Limited number of attempts
        if data[username] == password:  # if password matches then greeting the user
            print("Hello", username, ", Have a Good Day!")
            break
        else:  # If password does not matches then...
            print("""!!!WRONG PASSWORD!!!
            !!!ACCESS DENIED!!!""")
            print("Tries Left :", pass_flag)
            password = input("Enter your password :")
            pass_flag -= 1

elif operation == 2:
    new_username = input("Enter a new username :")  # Entering a new username
    while True:
        if new_username in data:
            print("This username already exists,")  # To ensure a new username and not an existing one
            new_username = input("Enter a new one :")
        else:
            break
    new_password = input("Enter a new password :")  # New password
    pass_confirm = input("Enter the password again for confirmation :")  # For confirming the password
    while True:
        if new_password != pass_confirm:  # for checking if the password matches
            print("The passwords don't match")
            new_password = input("Enter a new password :")
            pass_confirm = input("Enter the password again for confirmation :")
        else:
            break
    data[new_username] = new_password  # Inserting the data to the database
    print("Your Account was created Successfully!  Thanks for joining this Community")
else:
    print("Invalid input")
