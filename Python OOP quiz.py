from abc import ABC, abstractmethod

# Abstract class
class Employee(ABC):
    def __init__(self, name, salary):
        self.__name = name      # private attribute (encapsulation)
        self.__salary = salary  # private attribute

    def display_info(self):
        print("Employee Name:", self.__name)

    def get_salary(self):   # getter method (to access private salary)
        return self.__salary

    @abstractmethod
    def calculate_salary(self):
        pass


# Child class 1
class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return self.get_salary()  # full salary


# Child class 2
class PartTimeEmployee(Employee):
    def calculate_salary(self):
        return self.get_salary() / 2  # half salary


# Main program
emp1 = FullTimeEmployee("Alice", 50000)
emp2 = PartTimeEmployee("Bob", 50000)

employees = [emp1, emp2]

for emp in employees:
    emp.display_info()
    print("Calculated Salary:", emp.calculate_salary())
    print("-----")


Explanation of Concepts
🔹 1. Encapsulation
The attributes __name and __salary are private.
They cannot be accessed directly outside the class.
Access is controlled using a method like get_salary().
👉 This protects data from unwanted modification.
🔹 2. Inheritance
FullTimeEmployee and PartTimeEmployee inherit from Employee.
They reuse properties and methods (like display_info()).
👉 This avoids code duplication.
🔹 3. Abstraction
Employee is an abstract class using ABC.
It contains an abstract method calculate_salary() with no implementation.
👉 Forces subclasses to provide their own implementation.
🔹 4. Polymorphism
Both subclasses implement calculate_salary() differently:
FullTime → full salary
PartTime → half salary
Same method name, different behavior.
👉 This allows using one interface (calculate_salary()) for different types.
