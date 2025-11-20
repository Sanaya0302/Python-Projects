class parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
chiku=parrot("chiku",6)
piku=parrot("piku",7)
print(piku.name," is a ",piku.species)
print(chiku.name," is also a ",chiku.species)
print(piku.name," is ",piku.age)
print(chiku.name," is ",chiku.age)