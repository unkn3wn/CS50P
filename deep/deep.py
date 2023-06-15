# we take in input from a user than we will use string methods to get rid of any whitespace
# as well as make everthing lowercase
str = input("Whats the ... and Everything? ").casefold().strip();
# our if statement
if str == "42" or str == "forty-two" or str == "forty two":
    print("Yes")
else:
    print("no")