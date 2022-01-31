# Course number and course section: IS 115-3003
# Date of completion: 9/27/2020
# Brief explanation of the program: Input weight, conver to kilogram, grams
# milligrams, output the inputed weight, kilogram, gram, and milligram

weight=float(input("Enter your weight in pounds "))

#convert weight into kilogram, grams, milligrams
kilograms = weight/2.205
grams = weight * 454
milligrams = weight * 453592

#display the weight in pounds
print ("Your weight in pounds is" ,weight)
#display the weight in kilograms
print ("In kilograms, you weigh")
print (format(kilograms, '.2f'))
#display the weight in grams
print ("In grams, you weigh")
print (format(grams, '.2f'))
#display the weight in milligrams
print ("In milligrams, you weigh")
print (format(milligrams, '.2f'))
