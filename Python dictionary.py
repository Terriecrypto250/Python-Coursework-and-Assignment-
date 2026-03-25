def inventory_system():
    # Initialize an empty dictionary to store inventory
    # Key: item name, Value: quantity
    inventory = {}

    while True:
        print("\n--- Simple Inventory System ---")
        print("1. Add/Update Item")
        print("2. Retrieve Item Information")
        print("3. Display Total Quantity")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            name = input("Enter item name: ").strip().lower()
            try:
                quantity = int(input(f"Enter quantity for '{name}': "))
                
                # Update quantity if item exists, otherwise add it
                if name in inventory:
                    inventory[name] += quantity
                    print(f"Updated '{name}'. New total quantity: {inventory[name]}")
                else:
                    inventory[name] = quantity
                    print(f"Added '{name}' with quantity {quantity}.")
            except ValueError:
                print("Invalid input. Please enter a numeric value for quantity.")

        elif choice == '2':
            name = input("Enter item name to search: ").strip().lower()
            if name in inventory:
                print(f"Item: {name.capitalize()} | Quantity: {inventory[name]}")
            else:
                print(f"Error: '{name}' not found in inventory.")

        elif choice == '3':
            # Calculate the sum of all values in the dictionary
            total_items = sum(inventory.values())
            print(f"Total quantity of all items in inventory: {total_items}")

        elif choice == '4':
            print("Exiting system. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    inventory_system()
