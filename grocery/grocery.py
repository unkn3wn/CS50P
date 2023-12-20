def main():
    # Call the grocery function with an empty prompt
    grocery_item = grocery("")

def grocery(prompt):
    # Initialize an empty dictionary to store grocery items and their counts
    grocery_list = {}

    try:
        # Infinite loop to continuously prompt the user for grocery items
        while True:
            # Get user input and convert it to lowercase for case-insensitive comparison
            user_input = input(prompt).lower()

            # Check if the item is already in the grocery list
            if user_input in grocery_list:
                # If yes, increment the count
                grocery_list[user_input] += 1
            else:
                # If no, add the item to the grocery list with a count of 1
                grocery_list[user_input] = 1

    # Handle the end-of-file (EOF) error, usually triggered by Ctrl+D or Ctrl+Z
    except EOFError:
        # Print a newline for better formatting
        print("\n")

        # Iterate over the sorted keys of the grocery_list
        for item in sorted(grocery_list.keys()):
            # Print the count and item in uppercase
            print(f"{grocery_list[item]} {item.upper()}")

# Call the main function to start the program
main()
