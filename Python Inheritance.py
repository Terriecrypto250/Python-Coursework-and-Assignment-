#Base class - Animal
class Animal:

    # Method that prints fur message
    def fur(self):
        print("I have fur all over my body.")


# Dog class inherits from Animal
class Dog(Animal):

    # Method that prints barking message
    def bark(self):
        print("Dog barking.")


# Puppy class inherits from Dog
class Puppy(Dog):

    # Method that prints play message
    def play(self):
        print("I play all the time.")


# Create an instance of Puppy named bosco
bosco = Puppy()

# Call all three methods on bosco
bosco.play()  # from Puppy
bosco.bark()  # from Dog
bosco.fur()   # from Animal
