# we make our list dic
item_fruit = [
        {'Item': 'apple', 'Calories':'130'},
        {'Item':'Avocado', 'Calories':'50'},
        {'Item':'Kiwifruit', 'Calories':'90'},
        {'Item':'pear', 'Calories':'100'},
        {'Item':'Sweet Cherries', 'Calories':'100'},
]
# we get user input
user_item = input("Item: ")


# fruit is our varible for each iteration in our list dic.
for fruit in item_fruit:

        # if the users input matches any of the items in the list dict
       if user_item == fruit["Item"]:
        #        we print the item key value of Calories
               print("Calories:", fruit["Calories"])