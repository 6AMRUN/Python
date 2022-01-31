# Your name: Alexies Farinas
# Course number and course section: IS 115-3003
# Date of completion: 9/27/2020
# Brief explanation of the program: Input age, indicate whether person is infant,
# child, teenager, or adult. Using if,elif,else statements

age=float(input("Enter your age "))

if age <= 1:
    print("You are an infant.")
elif age >= 1 and age < 13:
    print ("You are a child.")
elif age > 13 and age <= 20:
    print("You are a teenager.")
else:
    print ("You are an adult")
    
