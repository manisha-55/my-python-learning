#Problem 1: Generate a list of squares from 1 to N using list comprehension
n=int(input("Enter N: "))
square_list= [i*i for i in range(1,n+1)]
print(square_list)

#Problem 2: Create a list of even numbers from 1 to 20 using list comprehension
evens= [i for i in range(1,21) if i%2==0]
print(evens)

#Problem 3: Use map() and lambda to convert Celsius to Fahrenheit  //Formula: F = (C × 9/5) + 32
# Enter Celsius temperatures separated by space: 0 20 37 100
# [32.0, 68.0, 98.6, 212.0]
c=[0,20,37,100]
f= list(map(lambda x:(x*9/50)+32, c))
print(f)

#Problem 4: Keep only numbers divisible by 3 (filter)
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
div_by_3 = list(filter(lambda x: x % 3 == 0, nums))
print(div_by_3)

#Problem 5: Product of all numbers (reduce)
from functools import reduce

nums = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, nums)
print(product)

#Problem 6: Exception Handling for Division
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
except ValueError:
    print("Error: Please enter valid integers")

#Problem 7: Combine map & filter (squares of even numbers)
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)))
print(even_squares)

#Problem 8: Length of strings using list comprehension
words = ["python", "java", "c", "javascript"]
lengths = [len(word) for word in words]
print(lengths)
