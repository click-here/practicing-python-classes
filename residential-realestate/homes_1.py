import statistics

class Home:

    def __init__(self, address, listingid, listprice):
        self.address = address
        self.listingid = listingid
        self.listprice = listprice
    
    def __repr__(self):
        return self.address

class State:

    def __init__(self, name, homes=None):
        self.name = name
        if homes == None:
            self.homes = []
        else:
            self.homes = homes

    def add_home(self, home):
        if home not in self.homes:
            self.homes.append(home)

    def homes_mean(self):
        return statistics.mean([x.listprice for x in self.homes])
        

pa = State('Pennsylvania')
pa_home1 = Home('401 Woodale Drive, Kennett Square, PA 19348','301259591223',900000)
pa_home2 = Home('928 Copes Lane, West Chester, PA 19380','301702687497',899900)
pa.add_home(pa_home1)
pa.add_home(pa_home2)

pa.__dict__
# > {'homes': [401 Woodale Drive, Kennett Square, PA 19348, 928 Copes Lane, West Chester, PA 19380], 'name': 'Pennsylvania'}

pa.homes_mean()
# > 899950.0