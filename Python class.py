# Class to handle temperature conversions
class Temperature:

    # Method to convert Celsius to Fahrenheit
    def convertFahrenheit(self, celsius):
        fahrenheit = (celsius * 9/5) + 32  # conversion formula
        print(f"{celsius}°C = {fahrenheit}°F")

    # Method to convert Fahrenheit to Celsius
    def convertCelsius(self, fahrenheit):
        celsius = (fahrenheit - 32) * 5/9  # conversion formula
        print(f"{fahrenheit}°F = {celsius:.2f}°C")

temp = Temperature()
temp.convertFahrenheit(100)
temp.convertCelsius(98.6)   


#Circle class
import math

# Class to represent a Circle
class Circle:

    def __init__(self, radius):
        self.radius = radius  # initialize with radius

    # Method to calculate area
    def area(self):
        result = math.pi * self.radius ** 2  # pi × r²
        print(f"Area = {result:.2f}")

    # Method to calculate circumference
    def circumference(self):
        result = 2 * math.pi * self.radius   # 2 × pi × r
        print(f"Circumference = {result:.2f}")

c = Circle(5)
c.area()     
c.circumference() 


#Class to represent a Bank Account
class BankAccount:

    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number  = account_number   # store account number
        self.balance         = balance          # store balance
        self.date_of_opening = date_of_opening  # store opening date
        self.customer_name   = customer_name    # store customer name

    # Method to deposit money
    def deposit(self, amount):
        self.balance += amount           # add amount to balance
        print(f"Deposited: ${amount}")
        return amount

    # Method to withdraw money
    def withdraw(self, amount):
        if self.balance < amount:        # check if balance is enough
            print("Insufficient balance")
        else:
            self.balance -= amount       # deduct amount
            print(f"Withdrawn: ${amount}")
            return amount

    # Method to check current balance
    def check_balance(self):
        print(f"Current Balance: ${self.balance}")

    # Method to print customer details
    def customer_details(self):
        print(f"Customer Name  : {self.customer_name}")
        print(f"Account Number : {self.account_number}")
        print(f"Date of Opening: {self.date_of_opening}")
        print(f"Balance        : ${self.balance}")

account = BankAccount("ACC001", 1000, "2024-01-15", "Terry")

account.deposit(500)  
account.withdraw(200)      
account.withdraw(5000)     
account.check_balance()     
account.customer_details()  
