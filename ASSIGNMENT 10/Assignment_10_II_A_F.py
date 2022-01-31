# Alexies Farinas
# 10/11/2020
# Program reads txt file, calculates the average and total, outputs an error whenever data is wrong

#Main Function
def main():
    total=0
    
#Reading File
    try:
        infile=open("numbers.txt" ,'r')
        
#For Loop
        for line in infile:
            amount=float(line)
            print(amount)
            total += amount
            average= total/amount
            
#Close File                  
        infile.close()

#Print Average and Total
        print("The total is " ,total)
        print ("The average is" ,average)
        
#Error output  
    except IOError:
        print("An error occured trying to read the file.")
    except ValueError:
        print("Non-numeric data found in the file.")

    except:
        print("An error occured.")
        
#Recalling Main Function
main()
