#area of a circle
import math

def area_circle(radius):
    return math.pi * radius ** 2

print(area_circle(7))


#area of a rectangle 
def area_rectangle(length, width):
    return length * width

print(area_rectangle(5, 3)) 


#volume of a cylinder
import math

def volume_cylinder(radius, height):
    return math.pi * radius ** 2 * height
  
print(volume_cylinder(3, 5)) 


#Sum of Elements in a List
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_list([1, 2, 3, 4]))  
