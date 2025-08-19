#1. Function to add two numbers
# def add(a,b):
#     return a+b
# result=add(4,4)
# print(result)

#2. Function to check if a number is prime
#the no is divisible by itself and 1
# def prime(a):
#     if a<=1:
#         return "Not Prime"
#     for i in range(2,a-1):
#         if(a%i==0):
#             return "Not prime"
#     return "Prime"
# print(prime(4))

#3. Function to return factorial (normal & recursion)
# n = int(input("Enter a number: "))
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)

# n = int(input("Enter a number: "))
# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(n))

#4. Reverse a string using function
# def reverse(str):
#     str=str[::-1]
#     return str
# print(reverse("manisha"))

#5. Check palindrome string using function
# def palindrome(str):
#     if str==str[::-1]:
#         return "Palindrome"
#     else:
#         return "Not Palindrome"
# print(palindrome("madam"))

#6. Find largest element in list using function
# n=int(input("Enter how many numbers of list: "))
# num=[]
# for _ in range(n):
#     val = int(input("enter numbers: "))
#     num.append(val)
# print(num)

# def largest(num):
#     max_num=num[0]
#     for i in num:
#         if i>max_num:
#             max_num=i
#     return max_num
#
# num=list(map(int, input("Enter numbers seperated by space: ").split()))
# print(num)
# print(largest(num))

#Problem 7: Count vowels in string
# def count_vowels(text):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for char in text:
#         if char in vowels:
#             count += 1
#     return count
#
# sentence = "Hello World"
# print("Vowel count:", count_vowels(sentence))


#Problem 8: List comprehension for squares
n = int(input("Enter num: "))
def squares_list(n):
    return [x**2 for x in range(1, n+1)]
print("Squares list:", squares_list(n))


