#Date of completion: 10/6/2020
#Brief explanation of the program: Enter the price of a many items the user want to purchase
# stop the loop if user enters '-1' and find the amount of items, total price, average price, cheapest price
# and the most expensive price of the items.

#Define the variables
itemQty= 0
minNum= 200
maxNum= 0
total= 0

#Define Item price
print("Enter the price of the item.")
itemPrice=int(input("Price: "))

#use sentinel loop to end the input loop
while itemPrice != -1:
    #If itemPrice is bigger than 200, message an error
    if itemPrice > 200:
        print("Enter the valid price of the item.")
    #Find the max and min  of the itemPrice
    if itemPrice < minNum:
        minNum= itemPrice
    elif itemPrice > maxNum:
        maxNum= itemPrice
    #Find total and Item Quantity
    total= total + itemPrice
    itemQty= itemQty + 1
    #To continue enter valid price, to stop enter '-1'
    print ("Enter the price of the item\nor enter -1 to stop")
    itemPrice= int(input("Price: "))

#Print the amount of items, total amount, average price, cheapest item, and most expensive item.
print("You are purchasing this amount of items:" ,itemQty)
print ("Your total for these items is $" ,format(total, ',.2f'), sep="")
print("The average total for the the items is $" ,format(total/itemQty, ',.2f'), sep="")
print("The cheapest item price you have is $" ,format(minNum, '.2f'), sep="")
print("The most expensive item price is " ,format(maxNum, '.2f'), sep="")

