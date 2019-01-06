#Conditionals are used to execute a line of code only if a certain condition is True

num1=int(input("Enter a number :"))
num2=int(input("Enter another number :"))

#If Condition
if True:
    print("The condition is True")

#if else condition
if(num1 > num2) :
    print(num1, "is greater than", num2)
else :
    print(num2, "is greater than", num1)

#Nested If Else
num3=int(input("Enter another number to compare with the first two :"))
if num1 > num2 :
    if num1 > num3 :
        print(num1, "is greatest")
    else:
        print(num3, "is greatest")
else :
    if num2 > num3 :
        print(num2, "is greatest")
    else:
        print(num3, "is greatest")

#Else If Ladder
#Another approach to find the largest
if num1 > num2 and num1 > num3:
    print(num1, "is greatest")
elif num2 > num1 and num2 > num3:
    print(num2, "is greatest")
else :
    print(num3, "is greatest")