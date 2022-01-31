# Your name: Alexies Farinas
# Course number and course section: IS 115-3003
# Date of completion: 9/28/2020
# Brief explanation of the program: User inputs the number of rooms booked
# if the number of rooms booked is at least 10, the discount is 10%; at least 20, the discount is 20%;
# and at least 30, the discount is 30%.
# if rooms are booked for at least 3 days, then there is an additional 5% discount

roomsBooked=float(input("Enter how many rooms you want to book "))
daysBooked=float(input("Enter how many days you are staying "))

print("The cost of renting one rooms is $100")
print("You have booked" ,roomsBooked, "rooms")
print("You have booked" ,daysBooked, "days")
rentPrice= (100 * roomsBooked *daysBooked)
print("The cost of the rooms before the discount is $", rentPrice)
salesTax= (13 * roomsBooked * daysBooked)
print("The sales tax is $" ,salesTax)

if roomsBooked >= 30:
    discount= .30
    print("You recieve a 30% discount")
    roomDiscount= rentPrice - (rentPrice * discount)
    finalPrice = roomDiscount + salesTax
elif roomsBooked >= 30 and daysBooked >=3:
    discount= .35
    print("The discount for each room is 35%")
    roomDiscount= rentPrice - (rentPrice * discount)
    finalPrice = roomDiscount + salesTax
elif roomsBooked >= 20:
    discount= .20
    print("You recieve a 20% discount")
    roomDiscount= rentPrice - (rentPrice * discount)
    finalPrice = roomDiscount + salesTax
elif roomsBooked >=20 and daysBooked >=3:
    discount= .25
    print("The discount for each room is 25%")
    roomDiscount= rentPrice - (rentPrice * discount)
    finalPrice = roomDiscount + salesTax
elif roomsBooked >= 10:
    discount= .10
    print("You recieve a 10% discount")
    roomDiscount= rentPrice - (rentPrice * discount)
    finalPrice = roomDiscount + salesTax
elif roomsBooked >=10 and daysBooked >=3:
    discount= .15
    print("The discount for each room is 15%")
    roomDiscount= rentPrice - (rentPrice * discount)
    finalPrice = roomDiscount + salesTax
else:
    finalPrice = rentPrice + salesTax

if daysBooked >=3:
    discount=.05
    print("You recieve a an additional 5% discount")
    roomDiscount= rentPrice - (rentPrice * discount)
    finalPrice = roomDiscount + salesTax
    
print("Please pay the total billing amount of $", finalPrice)
