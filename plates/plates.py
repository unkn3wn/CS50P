def main():
    # Get user input for the license plate.
    plate = input("Plate: ")
    
    # Check if the entered license plate is valid.
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    # Calculate the number of characters in the license plate.
    character_count = len(plate)

    # Check if the character count is between 2 and 6 (inclusive).
    if 2 <= character_count <= 6:
        # Check all the conditions for a valid license plate.
        if checkzero(plate) and check_nums_in_middle(plate) and starts_with_two_letter(plate) and check_for_punctuation(plate):
            return True

    # If any condition fails, return False.
    return False


# Check if zero is the first digit.
def checkzero(plate):
    # Iterate through the characters in the plate.
    for char in plate:
        # If the character is a digit, store it and stop.
        if char.isdigit():
            first_number = char
            break
    else:
        # Return True if no number is found.
        return True
    
    # Check if the first digit is not zero.
    return first_number != "0"


# Check if the plate starts with two letters.
def starts_with_two_letter(plate):
    # Get the first two characters of the plate.
    first_two_chars = plate[:2]
    
    # Return True if both characters are letters.
    return first_two_chars.isalpha()


# Check if there are no digits in the middle of the plate.
def check_nums_in_middle(plate):
    # Ensure that the plate has at least 4 characters.
    if len(plate) >= 4:
        middle_part = plate[2:-2]
        
        # Check if all characters in the middle part are digits.
        for char in middle_part:
            if char.isdigit():
                return False
    
    return True


# Check for any type of punctuation in the plate.
def check_for_punctuation(plate):
    # Define a string containing punctuation characters that are not allowed in the plate.
    punctuation = " .!?"
    
    # Iterate through each character in the punctuation string.
    for character in punctuation:
        # Check if the current punctuation character is present in the plate.
        if character in plate:
            # If found, return False indicating that the plate contains prohibited punctuation.
            return False
    
    # If no prohibited punctuation characters were found, return True.
    return True


# Call the main function to start the license plate validation process.
main()
