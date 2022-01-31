# Your name: Alexies Farinas
# Course number and course section: IS 115-3003
# Date of completion: 9/27/2020
# Brief explanation of the program: Enter the price for the meal
# calculate the amount along with a 18% tip and 7% sales tax
# display the amount of the meal price, tax, and tip and total price.

meal=float(input("Enter the price of the meal "))

#calculate the tip(18%)
tip= meal * .18
#calculate the sales tax (7%)
salesTax= meal * .07
#calculate the total price
totalAmount = meal + tip + salesTax

#display the meal price
print ("The price for the meal is")
print(format(meal, '.2f'))
#display the tip
print ("The tip for the meal is")
print(format (tip, '.2f'))
#display the sales tax
print("The sales tax is ")
print(format (salesTax, '.2f'))
#display the total amount for the meal
print("The total price for the meal is")
print(format (totalAmount, '.2f'))
