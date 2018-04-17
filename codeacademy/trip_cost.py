def hotel_cost(nights):
    return 140*nights


def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475


def rental_car_cost(days):
    cost = 40 * days
    if days >= 7:
        cost -= 50
    elif days >= 3:
        cost -= 20
    return cost


def trip_cost(city, days, spending_money):
    cost = plane_ride_cost(city) \
           + hotel_cost(days)\
           + rental_car_cost(days) \
           + spending_money
    return cost


c = input("Choose a city:\n")
d = int(input("How many days?\n"))
s = int(input("How much spending money?\n"))

total_cost = trip_cost(c, d, s)
print("Trip cost: ", total_cost)