#Lists are Similar to arrays in other languages but can hold different types of data
#Lists are defined using square braces

list1 = ["Jaideep", 18, 1.87]                         #Initializing Lists 1 and 2
list2=[1, 2, 9 ,4, 56 ,34]
print(len(list1))                                     #Gives the length of the list(Total no. of elements in the list)
print(type(list1))                                    #Gives the type of the variable

#Accessing
print(list1[0])                                       #Individual elements can be accessed using their index
print(list1[0:2])                                     #Range of elements can be accessed by specifying the range of index
print(list1[-1])                                      #Negative indexing(The index of the last element is -1 and of second element is -2 and so on)

#Inserting
list1.append("jaideepmore307@gmail.com")              #Inserts the element at the last position in the last
print(list1)
list1.insert(0, "Phoenix")                            #Inserts the element in the specified location
print(list1)
list1.extend(list2)                                   #Combines two lists together
print(list1)

#Deleting
list1.remove("Phoenix")                               #Deletes the specific element from the list
print(list1)
list1.pop()                                           #Deletes the last element from the list
print(list1)

#Sorting
list2.sort()                                          #Sorts the numbers in ascendng order and alphabets in alphabetical order
print(list2)
list2.sort(reverse=True)                              #Sorts the numbers in descending order and the alphaberts in reverse alphabetical order
print(list2)

#Searching
print(list1.index(18))                                #Returns the index of the first occuring element in the list
print("Phoenix" in list1)                             #Returns True if the element exists in the list else returns False

#Miscellaneous
print(max(list2))                                     #Returns the value of maximum element in the list
print(min(list2))                                     #Returns the value of minimum element in the list
print(sum(list2))                                     #Returns the summation the all the elemnts in the list
