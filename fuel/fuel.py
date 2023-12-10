# Define the main function to handle the fraction calculation and grading
def main():
    # Get a fraction from the user
    fraction = get_fraction("Fraction: ")
    
    # Split the fraction into numerator and denominator
    a, b = split_function(fraction)
    
    # Convert the fraction parts to integers
    a_int, b_int = convert_fraction(a, b, "Fraction: ")
    
    # Perform division and handle division by zero
    result_div = div_by_zero(a_int, b_int, "Fraction: ")
    
    # Display the final grade based on the division result
    answer = final_answer(result_div)

# Function to get a fraction from the user
def get_fraction(prompt):
    while True:
        fraction = input(prompt)
        if '/' in fraction:
            return fraction

# Function to split a fraction into numerator and denominator
def split_function(fraction):
    a, b = fraction.split("/")
    return a, b

# Function to convert fraction parts to integers
def convert_fraction(a, b, prompt):
    while True:
        try:
            if a.isnumeric() and b.isnumeric():
                a_int = int(a)
                b_int = int(b)
                return a_int, b_int
            else:
                # If conversion fails, prompt the user for a new fraction
                new_fraction = get_fraction(prompt)
                a, b = split_function(new_fraction)
        except ValueError:
            print("Error while converting fraction")

# Function to perform division and handle division by zero
def div_by_zero(a_int, b_int, prompt):
    while True:
        try:
            if a_int > b_int or b_int == 0:
                # If the denominator is zero or the numerator is greater than the denominator,
                # prompt the user for a new fraction
                new_fraction = get_fraction(prompt)
                a, b = split_function(new_fraction)
                a_int, b_int = convert_fraction(a, b, prompt)
            else:
                # Perform division and return the result
                result = a_int / b_int
                return result
        except ZeroDivisionError:
            print("Cannot divide by zero")

# Function to display the final grade based on the division result
def final_answer(result):
    # Convert the result to a percentage and round it
    percentage = round(result * 100)
    
    # Display the final grade based on the percentage
    if 90 <= percentage <= 100:
        print("F")
    elif 0 <= percentage <= 10:
        print("E")
    else:
        print(f"{percentage}%")

# Call the main function to start the program
main()
