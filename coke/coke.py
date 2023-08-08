# indicated amount we start with
total_due = 50
# indicated how much is due
amount_due = print("Amount Due:",total_due)


# this will keep looping until total_due = 0
while total_due != 0:

    # will keep looping to check if inserted coin is either a 5, 10, 15
    while True:
        # our input for coin
        inserted_coin = int(input("Insert Coin: "))
        # checks to see if inserted coin is either a 5, 10 ,25
        if inserted_coin in [5,10,25]:
            # if thats true it will break
            break
            #otherwise we will keep prompting for same amount die first with the insert coin statement
        else:
            print("Amount Due:",total_due)
    # the inserted coin will be supracted from the total amount due
    total_due = total_due - inserted_coin

    # now if total does not equal zero we w
    if total_due != 0 :
        print("Amount Due:",total_due)
        if total_due < 0 :
            total_due = total_due * -1
            print("Change Owed:",total_due)
    elif total_due == 0:
        print("Change Owed: 0")

print(total_due)