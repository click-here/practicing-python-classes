class Residence:

    def __init__(self, address):
        self.address = address


class Home(Residence):

    def __init__(self, address, listprice):
        super().__init__(address)
        self.listprice = listprice

    def set_foundation(self, foundation_type):
        self.foundation = foundation_type        

class Apartment(Residence):

    def __init__(self, address, monthly_rent):
        super().__init__(address)
        self.monthly_rent = monthly_rent

    def set_floornumber(self, floornumber):
        self.floornumber = floornumber  

h1 = Home('300 Diane Drive, West Chester, PA 19382',425000)
h1.set_foundation('Concrete Slab')

a1 = Apartment('202 Main St', 1200)
a1.set_floornumber(3)


print(h1.__dict__)
# > {'foundation': 'Concrete Slab', 'address': '300 Diane Drive, West Chester, PA 19382', 'listprice': 425000}
print(a1.__dict__)
# > {'monthly_rent': 1200, 'address': '202 Main St', 'floornumber': 3}