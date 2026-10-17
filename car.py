class Car:
    def __init__(self,brand,year):
      self.brand = brand
      self.year = year

car1 = Car("Toyota", 2020) 
car2 = Car("Honda", 2021)

print(car1.brand , car1.year )  # Output: Toyota 2020
print(car2.brand , car2.year )  # Output: Honda 2021


class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def describe(self):
        return f"Book: {self.title} is written by   {self.author}"    

book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

print(book1.describe())  # Output: 1984 is written by George Orwell
print(book2.describe())  # Output: To Kill a Mockingbird is written by Harper Lee