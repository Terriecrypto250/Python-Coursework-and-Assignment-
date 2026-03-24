# Prompting the user for input
hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate per hour: "))

# Calculating gross pay
gross_pay = hours * rate

# Displaying the result
print(f"Gross pay: {gross_pay}")


import math

# Prompting the user for the radius
radius = float(input("Enter the radius of the sphere: "))

# Calculating the volume using the formula (4/3) * pi * r^3
volume = (4/3) * math.pi * (radius ** 3)

# Displaying the result formatted to 2 decimal places
print(f"The volume of the sphere is: {volume:.2f}")
