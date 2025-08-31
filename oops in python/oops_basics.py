class Point:
    def __init__(self, x:float, y:float):
        self.x=x
        self.y=y
    def move(self, dx, dy):
        self.x+= dx
        self.y+= dy

p=Point(1,2)
p.move(3, -1)
print(p.x, p.y)

class Book:
    def __init__(self , title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def describe(self):
        return f"'{self.title}' by {self.author}, published in {self.year}"

book1 =Book("Harry Potter", "J.K ROWLINg", 1997)
print(book1.describe())


