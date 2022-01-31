##Date of completion: 10/7/2020
##Brief explanation of the program: Program generates 100 random numbers
## and counts how many of the random numbers are even and how many of them are
## odd

#Import random
import random

#main function
def main():
    
#count for the even and odd numbers
    even = 0;
    odd = 0;
    
#Range for the numbers
    for numbers in range(100):
        numList = (random.randint(0,1000))
        print(numList)
        if (numList%2) == 1:
            odd = odd+1
        if (numList%2) == 0:
            even = even+1
            
#output for even and odd amount of numbers
    print('number of evens is: ',even)
    print('number of odds is: ',odd)

#call the main function
main()
