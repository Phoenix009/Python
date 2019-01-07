#Functions allows programmer to keep the code dry
#If a set of code is being repeated in different parts of the code functions can be made

def get_data():
    name = input("Enter your name :")
    age = int(input("Enter your age :"))
    email = input("Enter your email :")
    return name, age, email

def put_data(name, age, email):                  #Parameterized Functions
                                                 #The variables in the braces are
    print("Name :", name)
    print("Age :", age)
    print("Email :", email)

name, age, email = get_data()
put_data(name, age, email)
