class Item:

    item_id = 1

    def __init__(self, name):
        self.name = name
        self.item_id = Item.item_id
        Item.item_id += 1

tv = Item('LG 42')
computer = Item('Dell XPS')

print(tv.item_id)
print(computer.item_id)

# prints:
# 1
# 2