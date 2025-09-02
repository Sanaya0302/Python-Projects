base=int(input("Enter base number: "))
exponent=int(input("Enter exponent number: "))
Power=base
for i in range(exponent -1 ):
    Power= Power *base
print("Power is",Power)



