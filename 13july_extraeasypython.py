# 1. Even or Odd
# Input a number → Output whether it’s "Even" or "Odd".
#n=int(input("Enter a number: "))
n=6
if(n%2==0):
    print(n,"is Even")
else:
    print(n,"is Odd")

# 2. Swap Two Variables (without using a third variable)
# Example: a = 5, b = 10 → a = 10, b = 5
a=5
b=10
a,b = b,a
print("swapping of 5 and 10 is:",a,b)

# 3. Area of a Circle
# Input: radius → Output: area (use math.pi).
import math
r=6
area = math.pi*(r**2)
print("area of a circle:",area)

# 4. Temperature Converter
# Convert Celsius → Fahrenheit and vice versa.
#F = (C * 9/5) + 32
c=10
f= (c* 9/5) +32
print("temp in fahrenheit:",f)

# 5. Check Leap Year
# Input: year → Output: True if leap year, else False.
# t=int(input("Enter a year: "))
# if(t%4==0 and t%400==0 or t%100!=0):
#     print("Leap Year")
# else:
#     print("Not Leap year")

# 6. Simple Calculator
# Input two numbers and an operator (+, -, *, /) → Output result.
# a=int(input("Enter 1st no: "))
# b=int(input("Enter 2nd no: "))
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

# 7. Factorial of a Number
# Input: 5 → Output: 120
a1=4
fact=1
for i in range(1, a1+1):
    fact*=i
print("factorial of",a1,"is:",fact)


# 8. Sum of Natural Numbers
# Input: n = 5 → Output: 15 (1+2+3+4+5)
#n=int(input("enter a no: "))
n=345
sum=0
while(n>0):
    ld=n%10
    n//=10
    sum+=ld
print(sum)

# 9. List of Squares
# Input: n = 5 → Output: [1, 4, 9, 16, 25]
number=5
list_of_squares=[i*i for i in range(1,number+1)]
print(list_of_squares)


# 10. Count Occurrences of a Character
# Input: "banana", "a" → Output: 3
str="banana"
ch='a'
count=0
for i in str:
    if(i==ch):
        count+=1
print(count)

# 11. Check if a String Contains Only Digits
# "12345" → True
# "12a45" → False
d1=12345
d2="12345"
#print(type(d1))
if d2.isdigit():
    print("true")
else:
    print("false")


# 12. Find Largest of Three Numbers
# Input: 10, 20, 15 → Output: 20
x=10
y=20
z=15
if(x>y and x>z):
    print("largest is",x)
elif(y>x and y>z):
    print("largest is",y)
else:
    print("largest is",z)

# 13. Multiplication Table
# Input: n = 3 → Output: 3 6 9 12 15 18 21 24 27 30
input_no =3
multiplication=0
for i in range(1,11):
    multiplication=input_no*i
    print(multiplication,end=' ')
print()


#14. Reverse a List (without using .reverse())
list1=[2,3,4,5]
rev_list=[]
for i in list1:
    rev_list.insert(0,i)
print(rev_list)

rev_list=list1[::-1]
print(rev_list)



# 15. Check Positive, Negative, or Zero
# Input: -5 → Output: "Negative"
inputnum=-5
if(inputnum>0):
    print("Positive")
else:
    print("Negative")
