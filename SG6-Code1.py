
# Start the program
#Declare three variables to store the input numbers as floating-point (decimal) values
#Example: float num1, float num2, float num3
#Display a message asking the user to enter the first number
#Get input from the user and store it in num1
#Display a message asking the user to enter the second number
#Get input from the user and store it in num2
#Display a message asking the user to enter the third number
#Get input from the user and store it in num3
#Add the three numbers and store the result in a new floating-point variable called sum
##sum = num1 + num2 + num3
#Display the value of sum to the user with appropriate formatting (e.g., two decimal places)
#End the program
#Expected Output:
#Enter the first number: 12.5
#Enter the second number: 8.25
#Enter the third number: 4.75
#The total of the three numbers is: 25.50

def float_sum(num1, num2, num3):
    sum = num1 + num2 + num3
    return sum
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
sum = float_sum(num1, num2, num3)

print(f"The total of the three numbers is: {sum:.2f}")