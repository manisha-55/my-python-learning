# class Student:
#     def __init__(self, name, add, roll):
#         self.name = name
#         self.roll = roll
#         self.add = add
#
#
# s1= Student("Manisha", "asd", 12)
# s2= Student("Shri", "asd", 12)
# s3= Student("Nidhish", "cty", 10)
# s4= Student("Manish", "trrg", 11)
#
# # s.name="Manisha"
# # s.add= "xfrg"
# # s.roll=12
# a=[]
# a.append(s1)
# a.append(s2)
# a.append(s3)
# a.append(s4)
#
# for i in a:
#     print(i.name, i.add, i.roll)
#
#
# l1 =[1,2,3,4]
# l2 =[5,6,7]
# for i in l2:
#     l1.append(i)
#
# print(l1)

start =1
end=10
for n in range(start, end+1):
    if n>1:
        for i in range(2,n):
            if(n%i==0):
                break
        else:
            print(n,end=" ")



