##Date of completion: 10/7/2020
##Brief explanation of the program: Program that accepts two integers from a
## user and uses the function mx to find out the larger number

#Input for two integers
int1 = int(input("Enter the first number: "))
int2 = int(input("Enter the second number: "))

#function mx
def mx(int1, int2):
    
    #If, else function defining whether or not the the values are greater of the two
    if int1 > int2:
        return int1
    else:
        return int2
    
#output for the max number
print("The max number is" ,mx(int1,int2))
