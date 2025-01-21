print("Welcome to the Prince Inventory Management System")
inventory = {}
total_items = 0

# Function to add items to the inventory
def add_item(item_name, quantity):
    global total_items
    if item_name in inventory:
        inventory[item_name] += quantity
    else:
        inventory[item_name] = quantity
    total_items += quantity
    print(f"Added {quantity} of {item_name}. Total items: {total_items}")

# Function to remove items from the inventory
def remove_item(item_name, quantity):
    global total_items
    if item_name in inventory:
        if inventory[item_name] >= quantity:
            inventory[item_name] -= quantity
            total_items -= quantity
            print(f"Removed {quantity} of {item_name}. Total items: {total_items}")
            if inventory[item_name] == 0:
                del inventory[item_name]
        else:
            print(f"Not enough {item_name} in inventory to remove.")
    else:
        print(f"{item_name} not found in inventory.")

# Function to display the inventory
def display_inventory():
    print("Current Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")
    print(f"Total items: {total_items}")

# Main Program
while True:
    print("\nInventory Management System")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Display Inventory")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        item_name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        add_item(item_name, quantity)
    elif choice == '2':
        item_name = input("Enter item name: ")
        quantity = int(input("Enter quantity: "))
        remove_item(item_name, quantity)
    elif choice == '3':
        display_inventory()
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")