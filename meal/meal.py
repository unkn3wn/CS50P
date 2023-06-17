def main():
    # 1. ask user for time
    time = input("Time? ")

    # 3. basically the find method for string
    if "a.m" in time or "p.m" in time:
        # we get our returns so we want the converted time and if its am or pm
        converted_time, morning_afternoon = convert(time)

        # check if its AM
        if morning_afternoon == "a.m":

            # if its AM it will alway be breakfast
            if  converted_time < 11.59:
                print("breakfast time")

        # check if its PM
        elif morning_afternoon == "p.m":

            # if its anywhere between 12- 5pm it will be lunch time
            if 12.00 <= converted_time <= 4.98:
                print("lunch time")
            # if its anywher between 5-11:59 pm it will be dinner time
            elif 5.00 <= converted_time <= 11.59:
                print("dinner time")

    # this will display if user does not include a a.m or a p.m
    else:
        time = input("Please include a.m or p.m: ")

# 2 .
def convert(time):
    # we want to split our hours and minutes
    hours, minutes = time.split(":")

    # convert hours into a float
    hours = float(hours)
    # split mintutes becuase we want to split the a.m or the p.m
    minutes, am_pm = minutes.split(" ")

    #convert the minutes into a float
    minutes = float(minutes)

    #set am_pm into a variable that we can return
    morning_afternoon = am_pm

    # divide and round our minutes into fraction form
    minutes = round(minutes / 60 , 2)

    #add hours and minutes
    time =  hours + minutes

    # return time, and the a.m p.m
    return time, morning_afternoon

if __name__ == "__main__":
    main()