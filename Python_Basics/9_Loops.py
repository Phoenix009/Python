#Loops are used to execute a set of code again and again until a condition in satisfied

for i in range(10):                       #Range specifies the limit
    print(i, ") Hello!")                  #The indentation(spaces) specifies the code in the for loop

print()
print()


i=0                                       #Initializing the counter
while(i<10):                              #Condition to be satisfied
    print(i, ") Hi!")
    i += 1                                #Incrementing the counter


#  !!ATTENTION!!
#the following is an infinite loop and will continue executing infinite times
#Stop the execution to avoid crashing

# i=0
# while True:
#     print(i)
#     i += 1