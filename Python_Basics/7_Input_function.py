#the input functions always returns string values

name=input("Enter Your Name :")                          #Taking user input
age=int(input("Enter Your Age :"))                       #Taking user input and converting into Integer
height=float(input("Enter your height in metres :"))     #Taking user input and converting into Float
print()
print()
print("Name :", name)
print("Your age :", age)
print("Your Height in metres :", height)
print("Datatype of name :", type(name))
print("Datatype of age :", type(age))
print("Datatype of height :", type(height))