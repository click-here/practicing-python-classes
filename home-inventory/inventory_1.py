class Item:

    item_location = "click-here's home"

    def __init__(self, name, home_location):
        self.name = name
        self.home_location = home_location

    def __str__(self):
        return "Item " + self.name


class Food(Item):
    def __init__(self, name, home_location='Kitchen'):
        self.name = name
        self.home_location = home_location

tv = Item('Sony TV','Living Room')
pizza = Food('Left over Dominos')

print(tv)
print(tv.name)
print(tv.home_location)
print(pizza)
print(pizza.name)
print(pizza.home_location)
