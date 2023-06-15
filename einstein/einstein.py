#create main function
def main():
    # ask user for mass
    x = float(input("M: "))
    # print the final answer of Joules
    print(f"E: {joules(x):.15f}")


# pass in a number, n will represent our mass
def joules(n):
    # perform Joules formula and return the result
    return n * pow(300000000, 2)

main()
