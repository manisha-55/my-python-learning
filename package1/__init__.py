# Input: [2, 3, 6, 6, 5]
# Highest = 6
# Runner-up = 5

n= list(map(int, input("Enter list: ").split()))
print(n)
highest=float('-inf')
for i in n:
    if(i>highest):
        highest=i
print(highest)
runner_up=float('-inf')
for i in n:
    if(i!=highest and i>runner_up):
        runner_up=i
print(runner_up)
