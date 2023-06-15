# tip Calculator
def main():
    #get total cost of meal
    dollars = dollars_to_float(input("How much was the meal? "))
    #get percentage of tip user wants to leave
    percent = percent_to_float(input("What percentage would you like to tip? "))
    #total cost of how much the meal will be with the tip cost
    tip = dollars * percent
    # print out the grand total
    print(f"Leave ${tip:.2f}")

#pass in the string
def dollars_to_float(d):
    # return number as a float by using strip method and rounding
    return round(float(d.strip("$")),2)


# pass in string of percent
def percent_to_float(p):
    # first we make the percentage into a whole number
   product = float(p.strip("%"))
   # than we divide by 100 to convert it into a decimal
   product = product /100
   # return the demial
   return product

main()