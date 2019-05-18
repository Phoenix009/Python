class Food:
    def __init__(self, name, price, calories):
        self.name = name
        self.price = price
        self.calories = calories

    def getCost(self):
        return self.price

    def getCalories(self):
        return self.calories

    def __str__(self):
        return str(self.name) + " : <" + str(self.price) + ", " + str(self.calories) + ">"


def prepareMenu(name, price, calories):
    menu = []
    for i in range(len(name)):
        menu.append(Food(name[i], price[i], calories[i]))
    return menu


def greedy(menu, maximize, keyFunction):
    itemsCopy = sorted(menu, key=keyFunction, reverse=True)

    totalCost, totalCalories = 0.0, 0.0
    result = []
    for i in range(len(menu)):
        if totalCalories + itemsCopy[i].getCalories() <= maximize:
            result.append(itemsCopy[i])
            totalCost += itemsCopy[i].getCost()
            totalCalories += itemsCopy[i].getCalories()

    return result, totalCost, totalCalories


name = ["Wine", "Pizza", "Burger", "fries", "coke", "apple", "donut"]
value = [89, 90, 30, 50, 90, 79, 90, 10]  # Cost
weight = [123, 154, 258, 354, 365, 150, 95, 195]  # Calories
menu = prepareMenu(name, value, weight)

finalorder, bill, calories = greedy(menu, 300, Food.getCost)
print("Bill :", bill, "Calories :", calories)
for i in finalorder:
    print(i)
