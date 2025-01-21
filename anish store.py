print("Welcome to Anish Shop".center(60))
print("This shop is for all the people".center(60))
print("We have all the things you need\n".center(60))

# Menu of items with their prices
prices = {
    1: ("Mobile", 20000),
    2: ("Laptop", 40000),
    3: ("Watch", 1000),
    4: ("Shoes", 2000),
    5: ("Clothes", 1500),
    6: ("Toys", 500),
    7: ("Books", 300),
    8: ("Pen", 50),
    9: ("Pencil", 10),
    10: ("Bag", 1000)
}

# Display the particular items available in the shop
print("Items available in the shop are:\n")
for number, (item, price) in prices.items():
    print(f"{number}. {item}: Rs. {price}")

# Initialize the total price
total_price = 0

# Get user input for numbers of the items to purchase
num_items = int(input("\nEnter the number of different items you want to purchase: "))

# Process each of the items purchased
for i in range(num_items):
    item_num = int(input(f"\nEnter the number of item {i + 1}: "))
    if item_num in prices:
        item_name, item_price = prices[item_num]
        quantity = int(input(f"Enter the quantity of {item_name}: "))
        total_price += item_price * quantity
    else:
        print(f"Item number {item_num} is not available. Please choose a valid item number.")

# Display the total price
print(f"\nTotal price for the selected items is: Rs. {total_price}")
print("\nThank you for shopping with us! Have a great day!".center(60))
