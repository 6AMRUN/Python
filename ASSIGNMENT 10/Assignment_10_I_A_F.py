# 10/11/2020
# Program opens notepad, user inputs 10 numbers, notepad is saved as a txt file.

#Main Function
def main():
#Defining name of the text file
    outfile = open("numbers.txt" ,"w")
    
#Input 10 numbers
    num1=int(input("Enter a number: "))
    num2=int(input("Enter a number: "))
    num3=int(input("Enter a number: "))
    num4=int(input("Enter a number: "))
    num5=int(input("Enter a number: "))
    num6=int(input("Enter a number: "))
    num7=int(input("Enter a number: "))
    num8=int(input("Enter a number: "))
    num9=int(input("Enter a number: "))
    num10=int(input("Enter a number: "))

    outfile.write(str(num1)+ '\n')
    outfile.write(str(num2)+ '\n')
    outfile.write(str(num3)+ '\n')
    outfile.write(str(num4)+ '\n')
    outfile.write(str(num5)+ '\n')
    outfile.write(str(num6)+ '\n')
    outfile.write(str(num7)+ '\n')
    outfile.write(str(num8)+ '\n')
    outfile.write(str(num9)+ '\n')
    outfile.write(str(num10)+ '\n')
#Closing text file
    outfile.close()
    print("Data written to numbers.txt")
#Recall main()
main()
