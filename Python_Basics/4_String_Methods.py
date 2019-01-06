message="Hello World"
print(message)
print(message[0])                                    #Prints the element at index 0
print(message[0:6])                                  #Prints the elements from index 0 to 5
print(message.lower())                               #Lowers all the elements n
print(message.upper())                               #Capitalizes all the elements
print(message.count("l"))                            #counts the number of the element "l"
print(message.find("W"))                             #returns the index of the first occuring "W"
new_message=message.replace("Hello", "Hi!")          #Replaces the word "Hello" by "Hi!"
print(new_message)
print(message + new_message)                         #Concatinates the string
print(message*3)                                     #Will Print the message thrice