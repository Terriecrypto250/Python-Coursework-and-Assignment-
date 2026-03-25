# Prompt user for 3 subjects
subject1 = float(input("Enter marks for subject 1: "))
subject2 = float(input("Enter marks for subject 2: "))
subject3 = float(input("Enter marks for subject 3: "))

# Compute the average
average = (subject1 + subject2 + subject3) / 3
print(f"Average Score: {average:.2f}")

# Grade average score
if average >= 70:
    print("Grade: A")
elif average >= 60:
    print("Grade: B")
elif average >= 50:
    print("Grade: C")
elif average >= 40:
    print("Grade: D")
else:
    print("Grade: Fail")


import random

# Bonus: Generate a random number between 1 and 100
winning_number = random.randint(1, 100)

# Ask user to guess
guess = int(input("Guess a number between 1 and 100: "))

# Check conditions
if guess == winning_number:
    print("YOU WIN !!!!")
else:
    if guess < winning_number:
        print("Too low")
    else:
        print("Too high")
    
    print(f"The actual number was: {winning_number}")
