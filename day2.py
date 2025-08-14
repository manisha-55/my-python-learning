# i=1
# while i<=5:
#     print(i)
#     i+=1

# Print numbers from 1 to 10 using for and while loop
# for i in range(1, 11):
#     print(i)

# a=1
# while(a<=10):
#     print(a)
#     a+=1

# for i in range(3):
#     for j in range(2):
#         print(i,j)


# Problem 1: Print Numbers from 1 to N
# Input: A number N
# Output: Print numbers from 1 to N using a loop

a= int(input("Enter the n number: "))
for i in range(1, a+1):
    print(i)

#  Problem 2: Sum of N Natural Numbers
# Input: A number N
# Output: Print the sum of numbers from 1 to N

a1= int(input("Enter the n number: "))
sum=0
for i in range(1,a1+1):
    sum+=i
print(sum)

# Problem 3: Count Digits in a Number
# Input: A number n
# Output: Number of digits in n
# Input: 12345
# Output: 5

# num= int(input("Enter the n number: "))
# num= abs(num)
# count=0
# while(num>0):
#     num=num//10
#     count+=1
# print(count)

#  Problem 4: Reverse a Number
# Input: A number n
# Output: Reverse of n
# Input: 123
# Output: 321

# n= int(input("Enter the n number: "))
# rev=0
# while(n>0):
#     ld= n%10
#     n=n//10
#     rev=rev*10+ld
# print(rev)

# Problem 5: Print This Pattern (stars)
# Input: 4
# Output:
# *
# * *
# * * *
# * * * *
# n= int(input("Enter the n number: "))
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# Problem 6: Print This Pattern (numbers)
# Input: 4
# Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4

# n= int(input("Enter the n number: "))
# for i in range(1, n+1):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print()

# Problem 7: Find Max in a List
# Input: A list of numbers
# Output: Maximum value in the list
# Input: [5, 8, 2, 9, 1]
# Output: 9

# list = [5,8,2,9,1]
# max = list[0]
# for i in list:
#     if(i>max):
#         max =i
# print(max)

# list = [5,8,2,9,1]
# max = list[0]
# for i in range(len(list)):
#     if(list[i]>max):
#         max=list[i]
# print(max)

# Problem 8: Count Even and Odd Numbers in a List
# Input: A list of integers
# Output: Count of even and odd numbers separately
# Input: [1, 2, 3, 4, 5]
# Output: Even: 2 Odd: 3

l1 = [1,2,3,4,5]
even=0
odd=0
for i in l1:
    if(i%2==0):
        even+=1
    else:
        odd+=1
print("Even:",even,"Odd:",odd)





