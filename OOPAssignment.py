# Assignment 1
class Book:
    def __init__(self, title, author, no_of_pages):
        self.title = title
        self.author = author
        self.no_of_pages = no_of_pages
    
    def make_order(self, order_no):
        print(f"{self.title} has been ordered with order number {order_no}...")
    
    def get_info(self):
        return f"Title: {self.title}, Author: {self.author}, No of Pages: {self.no_of_pages}pages"


class Novel(Book):
    def __init__(self, title, author, no_of_pages, point_of_view):
        super().__init__(title, author, no_of_pages)
        self.point_of_view = point_of_view

    def get_info(self):
        return f"{super().get_info()}"
    
    def make_order(self, order_no):
        print(f"{self.title} with order number {order_no} is going through some price changes")

book = Book("Paranoia", "Lily Borton", 456)
novel = Novel("Summer of Love", "Noel Mitchel", 348, "First Person POV")

print(book.get_info())
book.make_order("012987")

print(novel.get_info())
novel.make_order("012988")

# Activity 2

class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Driving")

class Plane(Vehicle):
    def move(self):
        print("Flying")

class Boat(Vehicle):
    def move(self):
        print("Sailing")

vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
