#1. Create a dictionary of student details and print them.
student = {"name": "Shrinidhi", "age":4, "class":"LKG"}
print(student)

#Update a dictionary with new key-value pairs.
student["City"]= "Pune"
student["age"]= 5
print(student)

#Count frequency of each word in a string using dictionary.
#o/p: {'python': 3, 'java': 2, 'c': 1}
#n= input("Enter a string: ")
n="python java python c java python"
words=n.split()
count ={}
print(words)
for i in words:
    if i in count:
        count[i]+=1
    else:
        count[i]= 1

print(count)

#Problem 4: Create a set of numbers and perform union & intersection
A= {1, 2, 3}
B={3, 4, 5}
print(A.union(B))
print(A.intersection(B))

#Problem 5: Remove duplicates from a list using set
list1= [1, 2, 2, 3, 4, 4, 5]
print(list1)
my_set = set(list1)
print(my_set)

#Problem 6: Read a text file and print its contents
file =open(r"C:\Users\Asus\OneDrive\Desktop\prg1.txt",'r')
content = file.read()
print(content)
file.close()

#Problem 7: Write user input to a file
file =open(r"C:\Users\Asus\OneDrive\Desktop\prg1.txt",'w')
file.write(input("Enter text to write in file: "))
file.close()

#Problem 8: Append new content to an existing file
#IP: Enter text to append: Adding more notes here. ##OP: Learning Python is fun!

file =open(r"C:\Users\Asus\OneDrive\Desktop\prg1.txt",'a')
file.write(input("Enter text to append in file: "))
file.close()








