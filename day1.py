# Problem 1: Basic Calculator
# Input: Two numbers and an operator (+, -, *, /)

# num1 = int(input("Enter num 1: "))
# num2 = int(input("Enter num 2: "))
# print("Addition is: ",num1+num2)
# print("Subtraction is: ",num1-num2)
# print("Multiplication is: ",num1*num2)
# if num2 != 0:
#     print("DIvision is: ",num1/num2)
# else:
#     print("cannot divide by 0")

#  Problem 2: Find the Greatest of 3 Numbers
# Input: 3 numbers

# a = int(input("Enter num 1: "))
# b = int(input("Enter num 2: "))
# c = int(input("Enter num 3: "))
# if (a>b and a>c):
#     print("A is greatest number")
# elif(b>a and b>c):
#     print("B is the greatest number")
# else:
#     print("C is the greatest number")

# Problem 3: Check if a number is divisible by both 5 and 11
# Input: 1 number
# Output: Yes or No

# a = int(input("Enter number: "))
# if(a%5==0 and a%11==0):
#     print("Yes")
# else:
#     print("No")

# Problem 4: Check Leap Year
# Input: A year (integer)
# Output: "Leap year" or "Not a leap year"
# A year is a leap year if:
# Divisible by 400, OR
# Divisible by 4 and not divisible by 100
# Input: 2020 → Output: Leap year
# Input: 1900 → Output: Not a leap year

# year = int(input("Enter a year: "))
# if year%400==0 or (year%4==0 and year%100!=0):
#     print("Leap year")
# else:
#     print("Not a leap year")

# Problem 5: Grading System
# Input: Marks (0–100)
# Output: Grade using if-elif-else
# Grading Rules:
# Marks >= 90 → Grade A
# Marks >= 75 → Grade B
# Marks >= 60 → Grade C
# Marks >= 40 → Grade D
# Else → Fail

# marks = int(input("Enter marks bet 0 to 100: "))
# while (marks<0 or marks>100):
#     print("invalid marks")
#     marks = int(input("enter valid marks: "))
# if (marks>=90):
#     print("Grade A")
# elif (marks>=75 and marks<90):
#     print("Grade B")
# elif (marks>=60 and marks<75):
#     print("Grade C")
# elif(marks>=40 and marks<60):
#     print("Grade D")
# else:
#     print("Failed")

# Problem 6: Simple Interest Calculator
# Input: Principal (P), Rate (R), Time (T)
# Output: Simple Interest = (P × R × T) / 100

# p = float(input("Enter principal:"))
# r = float(input("enter rate:"))
# t = float(input("enter time:"))
# si = (p*r*t)/100
# print("Simple Interest =",si)

# Problem 7: Check Positive, Negative or Zero
# Input: One integer
# Output: "Positive", "Negative" or "Zero"

# a = int(input("Enter a number: "))
# if (a>0):
#     print("Positive")
# elif (a==0):
#     print("Zero")
# else:
#     print("Negative")

#  Problem 8: Triangle Type Checker
# Input: 3 sides of triangle
# Output:
# "Equilateral" (all sides equal)
# "Isosceles" (two sides equal)
# "Scalene" (no sides equal)

s1 =int(input("enter side1: "))
s2 =int(input("enter side2: "))
s3 =int(input("enter side3: "))
if(s1==s2 and s2==s3):
    print("Equilateral")
elif(s1==s2 or s2==s3 or s1==s3):
    print("Isosceles")
else:
    print("Scalene")


