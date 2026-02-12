#Part A:                Variables & Data types
#Question # 01:
#Create a variable and store your name in it. Print the variable.
#Answer:
# Code
my_name = “ Ruqqaya Noor”
Print(my_name)


#Question # 02:
#Create two variables age and height. Print both values?
#Answer:
# Code
# Define variables
Age =19
 height=  6
# Print the values
Print(“Age:” , age)
Print(“height:” , height)

#Question # 3:
#Store a number in a variable and print its data type using type()
# Define a variable with a number
Num = 78
# print the data type of the variable
Print(type(num))

#Question # 4:
#Create a variable is_student and store True in it. Print the values?
#Answer:
# Coding
Is_student = True
Print(is_student)

#Question # 5:
#Take one number from the user and store it in a variable. Print the number?
#Answer:
# Coding
# Get input from the user
num = input(“Enter a number:”)
# print the number
Print(num)

#Part B:   Operators and conditional stament
#Question # 6
#Take two numbers from the user and print their sum?
#Answer:
# Coding
# Get two numbers from the user
num1 = int(“Enter first number:”)
num2 = int(“Enter second number:”)
# Calculate the sum
Sum = num1 + num2
# print the result
Print(“The sum of “ , num1, “and” , num2, “is: “ , sum)

#Question # 7:
#Take two numbers and check which one is greater using if?
# Answer:
# Coding
# input two numbers
num1 = float(input(“Enter first number:”))
num2 = float(input(“Enter second number:”))
# Comparison using if-else
If num1 > num2
	Print(f”{num1} is greater than {num2}”)
else  num2>num1
	print(f”{num2}  is greater than {num1}”)

#Question # 8:
#Take one number and check whether it is even or odd?
#Answer:
# Coding
Def check_even_odd(num):
num = int(input(“Enter a number:”))
	If num % 2== 0:
		Print(f”{num} is even”)
	else :
		print(f”{num} is odd”)

#Question #  9:
#Take marks as an input and print pass if marks are 50 or above fail otherwise?
#Answer:
# Code
marks = int(input(“Enter your marks:”))
if marks >= 50
	print(“pass”)
else 
	print(“fail”)
#Question # 10:
#Take a number and check: whether it is less than 10, equal to 10 or greater than 10?
#Answer:
num = int(input(“Enter a number:”))
if num < 10:
	print(“Less than 10”)
else if num == 10:
	print(“Equal to 10”)
else:
	print(“Greater than 10”)


#Project:    To check the positive or negative number
#Question:
#Take a number from the user and check whether it is positive or negative.
#Answer:
# Code
num = int(iput("Enter a number:"))
if num >=0:
        print("Postive number")
     else 
        print("Negative number")   

