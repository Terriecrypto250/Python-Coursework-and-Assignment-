# Create an empty list to store inventory items
inventory = []

# Ask user how many items to add
n = int(input("How many items do you want to add? "))

# Loop to collect each item name and quantity
for i in range(n):
    item = input(f"Enter item name {i + 1}: ")
    quantity = int(input(f"Enter quantity for {item}: "))
    # Add item and quantity as a pair into the list
    inventory.append([item, quantity])

# Ask user to search for a specific item
search = input("\nEnter item name to retrieve info: ")

# Loop through inventory to find the item
for i in range(len(inventory)):
    if inventory[i][0] == search:
        print(f"{search}: {inventory[i][1]} in stock")
        break
    elif i == len(inventory) - 1:
        print(f"{search} not found in inventory.")

# Calculate total quantity of all items
total = 0
for i in range(len(inventory)):
    total += inventory[i][1]

# Display full inventory and total
print("\nFull Inventory:", inventory)
print("Total quantity of all items:", total)
