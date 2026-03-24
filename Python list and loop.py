names = []

n = int(input("How many names do you want to enter? "))

for i in range(n):
    name = input(f"Enter name {i + 1}: ")
    names.append(name)

# Remove duplicates and sort alphabetically
names = sorted(set(names))

print("\nSorted names (no duplicates):", names)
print("Total number of names:", len(names))
