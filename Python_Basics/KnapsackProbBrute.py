class Food:
    def __init__(self, name, value, weight):
        self.name = name
        self.value = value  # cost of the food item
        self.weight = weight  # Calories associated with that item

    def getValue(self):
        return self.value

    def getWeight(self):
        return self.weight

    def density(self):
        return self.value / self.weight

    def __str__(self):
        return str(self.name) + " : <" + str(self.value) + ", " + str(self.weight) + ">"


"""Function to prepare a menu"""


def prepareMenu(name, value, weight):
    menu = []
    for i in range(len(name)):
        menu.append(Food(name[i], value[i], weight[i]))
    print("The menu prepared is : ")
    for i in menu:
        print(i)
    return menu


def greedy(items, maxWeight, keyFunction):
    itemsCopy = sorted(items, key=keyFunction, reverse=True)
    result = []
    totalValue, totalWeight = 0.0, 0.0

    print("The sorted menu : ")
    for i in itemsCopy:
        print(i)
    for i in range(len(itemsCopy)):
        if totalWeight + itemsCopy[i].weight <= maxWeight:
            result.append(itemsCopy[i])
            totalValue += itemsCopy[i].value
            totalWeight += itemsCopy[i].weight

    return (result, totalValue, totalWeight)


name = ["Wine", "Pizza", "Burger", "fries", "coke", "apple", "donut"]
value = [89, 90, 30, 50, 90, 79, 90, 10]  # Cost
weight = [123, 154, 258, 354, 365, 150, 95, 195]
# Calories
menu = prepareMenu(name, value, weight)

finalorder, bill, calories = greedy(menu, 300, Food.getValue)  # Optimizes best order for cost below 700
print("The suitable order : ")
print("Rs :", bill, "Calories :", calories)
for i in finalorder:
    print(i)
