#Dictionaries are defined with curly braces

data = {"name": "Jaideep_More", "age": 18, "email": "jaideepmore307@gmail.com"}                     #SYNTAX  key : value
print(len(data))
print(data.keys())
print(data.values())
print("Name :", data["name"])
print("Age :", data["age"])
print("Email :", data["email"])

#Inserting
data["Salary"] = 180000
print(data)
data.update({"height_m" : "1.87"})
print(data)

#Deleting
popped=data.pop("name")
print(data)
print(popped)
del data["email"]
print(data)