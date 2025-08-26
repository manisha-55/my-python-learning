####### Instance variable and Static Variable.
class Car:
    wheels = 4     ########### static variable

    def __init__(self):
        self.mil = 10
        self.com = "BMW"

c1= Car()
c2= Car()

c1.mil = 8
Car.wheels = 5

print(c1.com, c1.mil, c1.wheels)
print(c2.com, c2.mil, c2.wheels)


################# Instance Method Type Example
class Student:
    school = 'Telusko'
    def __init__(self, m1, m2, m3):
        self.m1 =m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3

s1= Student(78, 89, 88)
s2= Student(67, 89, 84)
print(s1.avg())

################# Class Method Type Example
class Student:
    school = 'Telusko'
    def __init__(self, m1, m2, m3):
        self.m1 =m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    @classmethod
    def info(cls):
        return cls.school

s1= Student(78, 89, 88)
s2= Student(67, 89, 84)
print(s1.avg())
print(s1.info())
print(Student.info())