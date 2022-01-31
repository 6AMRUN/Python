##Date of completion: 10/7/2020
##Brief explanation of the program: Nested loops to collect data and calculate
## the average rainfall over a period of years.


#Declare the variables for total rainfall, average rainfall, and years
totalRainfall= 0
avgRainfall= 0
years= 0

#Get the number years
years=int(input("Enter the number of years "))

#Loop for rainfall by month by 3 iterations
for year in range(years):
    totalMonths= 0
    print ("For year" ,year + 1)
    for month in range(3):
        monthRainfall = float(input("Enter the rainfall amount for the month: "))
        totalMonths += 1
        totalRainfall += monthRainfall
        avgRainfall = totalRainfall / totalMonths
        
#print for totalRainfall, avgRainfall
    print("For" ,totalMonths, "months")
    print("Total rainfall: " ,totalRainfall)
    print("Average rainfall for" ,year + 1, "is: " ,avgRainfall)
