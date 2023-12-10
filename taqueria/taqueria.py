# Define a menu with food items and their prices
menu = {
    "baja taco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}

# Define the main function to handle the order processing
def main():
    total = 0  # Initialize the total cost to zero
    try:
        # Start an infinite loop to continuously take customer orders
        while True:
            customer_item = get_item("Item: ")  # Get the customer's selected item
            item_price = get_item_price(menu, customer_item)  # Get the price of the selected item
            total = adding_items(total, item_price)  # Add the item price to the total
            print(f"Total: ${total:.2f}")  # Display the updated total with two decimal places
    except EOFError:
        pass  # Catch the end-of-file error (e.g., Ctrl+D on the keyboard) to exit the loop gracefully

# Define a function to get a valid item from the customer
def get_item(prompt):
    try:
        while True:
            customer_item = input(prompt).lower()  # Get the customer's input and convert to lowercase
            if customer_item in menu:
                return customer_item  # If the item is in the menu, return it
            else:
                print("Invalid item. Please try again.")  # If not, prompt the customer to try again

    except ValueError:
        print("Error getting item")  # Handle any errors that might occur while getting the item

# Define a function to get the price of a given item from the menu
def get_item_price(menu, customer_item):
    try:
        for item, price in menu.items():
            if customer_item == item:
                return price  # If the item is found in the menu, return its price

    except:
        print("Error Getting price of item")  # Handle any errors that might occur while getting the price

# Define a function to add the price of an item to the total
def adding_items(total, price):
    total += price  # Add the price of the item to the total
    return total  # Return the updated total

# Call the main function to start the order processing
main()
