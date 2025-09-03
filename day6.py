# 1. Even/Odd Counter
#a = list(map(int, input().split()))
a = [3,4,5,6]
print(a)
even=0
odd=0
for i in a:
    if(i%2==0):
        even+=1
    else:
        odd+=1

print("Even:",even, "Odd:",odd)

# 2. Word Frequency Counter
n= input("Enter a string: ")   #text = "python java python c java python"
word = n.split()
dict ={}
for i in word:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1

print(dict)
