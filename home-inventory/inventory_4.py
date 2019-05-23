class Item:

    def __init__(self, name, home_location):
        self.name = name
        self.home_location = home_location

class Food(Item):

    def __init__(self, name, calories, home_location='Kitchen'):
        super().__init__(name, home_location)
        self.home_location = home_location
        self.calories = calories

pizza = Food('Left over Dominos',200)

print(pizza.__dict__)
# > {'calories': 200, 'home_location': 'Kitchen', 'name': 'Left over Dominos'}
