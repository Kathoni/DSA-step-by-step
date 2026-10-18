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


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def check_result(self):
        if self.marks >= 50:
            print(f"{self.name} has passed!")
        else:
            print(f"{self.name} has failed.")


student1 = Student("Sylvia", 75)
student2 = Student("Brian", 35)

student1.check_result()
student2.check_result()


class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount: float) -> str:
        # Control flow inside a method
        if amount <= 0:
            return "Withdrawal amount must be positive."
        elif amount > self.balance:
            return f"Insufficient funds! Current balance: ${self.balance}"
        else:
            self.balance -= amount
            return f"Withdrew ${amount}. Remaining balance: ${self.balance}"

account = BankAccount("Alice", balance=100.0)
print(account.withdraw(150))  # Output: Insufficient funds! Current balance: $100.0
print(account.withdraw(40))   # Output: Withdrew $40. Remaining balance: $60.0