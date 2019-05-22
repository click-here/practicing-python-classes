class Item:

    @classmethod
    def create_roomless(cls, name):
        return cls(name, home_location=None)

    @classmethod
    def create_multiroom(cls, name, rooms):
        return cls(name, home_location=list(rooms))

    def __init__(self, name, home_location):
        self.name = name
        self.home_location = home_location 
        
item_list = [
    Item('LG 42', 'Living Room'),
    Item('Dell XPS', 'Office'),
    Item.create_roomless('Casio Watch'),
    Item.create_multiroom('Wall in Fish Tank',['Living Room','Sun Room'])
]

for i in item_list:
    print(i.home_location)

# Prints
# Living Room
# Office
# None
# ['Living Room','Sun Room']