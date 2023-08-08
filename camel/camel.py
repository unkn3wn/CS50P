camelCase = input("camelCase: ")
snake_case = ""
# loop through each letter and find uppercase
# if no upper case return word as is

# i in this case is our variable for each iteration of the input
for i in camelCase:

    # check if there is a upper case
    if i.isupper():

        # store the upper case into a varibale
        cap_letter = i
        # add a underscore before the uppercase than make it to lowercase
        snake_case = "_" + i.lower()

        # we replace the uppercase with out snake_case letter
        camelCase = camelCase.replace(cap_letter, snake_case)
        # print out new word but with snake_case
        print(camelCase)

    else:
        # if no upper case we just return word as is 
        print( i, end="")




