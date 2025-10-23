def hotel_cost(nights):
    return 120*nights
def plane_ride_cost(country):
    if country=="USA":
        return 1900
    elif country=="Australia":
        return 1500
    elif country=="Japan":
        return 2300
    elif country=="South Korea":
        return 2400
def rental_car_cost(days):
    if days>=7:
        return 40*days-50
    elif days>=3:
        return 40*days-20
    else:
        return 40*days
def total_cost(country,days,spending_money):
    return hotel_cost(days)+rental_car_cost(days)+plane_ride_cost(country)+spending_money
print("rental car cost is",rental_car_cost(6))
print("plane ride cost is",plane_ride_cost("Japan"))
print("total cost is",total_cost("Japan",6,1500"))



