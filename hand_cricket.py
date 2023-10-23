import random as rnd
print("\t HAND CRICKET")

# TOSS
print("\n 1.ODD \n 2.EVEN")

# Getting user choice for odd or even
while True:
    try:
        oe = int(input("Choose ODD or EVEN (1 or 2): "))
        if oe not in [1, 2]:
            raise ValueError
        break
    except ValueError:
        print("Invalid choice. Please choose 1 for ODD or 2 for EVEN.")

if oe == 1:
    print("you have chosen ODD")
else:
    print("you have chosen EVEN")

print("\n \t TOSS \n")

# Getting user's toss input
while True:
    try:
        toss_user = int(input("Enter a number between 1 to 6 for the toss: "))
        if toss_user not in range(1, 7):
            raise ValueError
        break
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 6.")

# Generate a random number for computer's toss
toss_comp = rnd.randint(1, 6)
toss_total = toss_user + toss_comp
toss = oe == 1 and (toss_total) % 2 != 0 or oe == 2 and (toss_total) % 2 == 0

# Determining the toss result
if toss:
    print(f"{toss_total} - you have won the toss")
    print("\n 1.BAT \n 2.BOWL")

    # Getting user's choice for batting or bowling
    while True:
        try:
            user_choice = int(input("Choose to BAT or BOWL (1 or 2): "))
            if user_choice not in [1, 2]:
                raise ValueError
            break
        except ValueError:
            print("Invalid choice. Please choose 1 for BAT or 2 for BOWL.")

    comp_choice = 1 if user_choice == 2 else 2

    if user_choice == 1:
        print("\n you have chosen to bat")
        print(" computer is bowling")
    else:
        print("\n you have chosen to bowl")
        print(" computer is batting")
else:
    print(str(toss_total) + " - computer has won the toss")
    comp_choice = rnd.choice([1, 2])
    user_choice = 1 if comp_choice == 2 else 2
    if comp_choice == 1:
        print("\n computer has chosen to bat")
        print(" you are bowling")
    else:
        print("\n computer has chosen to bowl")
        print(" you are batting")

# MATCH
print("\n \t MATCH BEGINS!!! \n")

user_runs_total, comp_runs_total = 0, 0
user_ball_count, comp_ball_count = 1, 1
user_out, comp_out = False, False

# User's choice is to bat
if user_choice == 1:
    # USER BATTING
    while user_out != True:
        print(f"User is batting - Ball no : {comp_ball_count}")

        # Getting user input for the runs scored
        while True:
            try:
                user_runs = int(input("Enter a number between 1 to 6 to bat : "))
                if user_runs not in range(1, 7):
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 6.")

        # Simulating the computer's ball
        comp_ball = rnd.randint(1, 6)
        if user_runs != comp_ball:
            print(f"\t BALL : {comp_ball}\t RUN : {user_runs}")
            user_runs_total += user_runs
            print(f"\t TOTAL RUNS : {user_runs_total} \n")
            comp_ball_count += 1
        else:
            print(f"\t BALL : {comp_ball}\t RUN : {user_runs}")
            print("\t \t !!!OUT!!!")
            print(f"\t TOTAL RUNS : {user_runs_total}")
            user_out = True

    # TARGET
    print(f"\n \t TARGET : {user_runs_total + 1} \n")

    # USER BOWLING
    while comp_out != True:
        print(f"Computer is batting - Ball no : {user_ball_count}")

        # Getting user input for the ball bowled
        while True:
            try:
                user_ball = int(input("Enter a number between 1 to 6 to bowl : "))
                if user_ball not in range(1, 7):
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 6.")

        # Simulating the computer's runs
        comp_runs = rnd.randint(1, 6)
        if comp_runs != user_ball:
            print(f"\t BALL: {user_ball}\t RUN : {comp_runs}")
            comp_runs_total += comp_runs
            print(f"\t TARGET : {user_runs_total + 1} \t TOTAL RUNS : {comp_runs_total} \n")
            user_ball_count += 1
            if comp_runs_total > user_runs_total:
                print("\n \t COMPUTER WON :(")
                break
        else:
            print(f"\t BALL: {user_ball}\t RUN : {comp_runs}")
            print("\t \t !!!OUT!!!")
            print(f"\t TARGET : {user_runs_total + 1} \t TOTAL RUNS : {comp_runs_total}")
            if comp_runs_total > user_runs_total:
                print("\n \t COMPUTER WON :(")
            else:
                print("\n \t !!!YOU WON!!!")
            comp_out = True
else:
    # USER BOWLING
    while comp_out != True:
        print(f"Computer is batting - Ball no : {user_ball_count}")

        # Getting user input for the ball bowled
        while True:
            try:
                user_ball = int(input("Enter a number between 1 to 6 to bowl : "))
                if user_ball not in range(1, 7):
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 6.")

        # Simulating the computer's runs
        comp_runs = rnd.randint(1, 6)
        if comp_runs != user_ball:
            print(f"\t BALL: {user_ball}\t RUN : {comp_runs}")
            comp_runs_total += comp_runs
            print(f"\t TOTAL RUNS : {comp_runs_total} \n")
            user_ball_count += 1
        else:
            print(f"\t BALL: {user_ball}\t RUN : {comp_runs}")
            print("\t \t !!!OUT!!!")
            print(f"\t TOTAL RUNS : {comp_runs_total}")
            comp_out = True

    # TARGET
    print(f"\n \t TARGET : {comp_runs_total + 1} \n")

    # USER BATTING
    while user_out != True:
        print(f"User is batting - Ball no : {comp_ball_count}")

        # Getting user input for the runs scored
        while True:
            try:
                user_runs = int(input("Enter a number between 1 to 6 to bat : "))
                if user_runs not in range(1, 7):
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 6.")

        # Simulating the computer's ball
        comp_ball = rnd.randint(1, 6)
        if user_runs != comp_ball:
            print(f"\t BALL : {comp_ball}\t RUN : {user_runs}")
            user_runs_total += user_runs
            print(f"\t TARGET : {comp_runs_total + 1} \t TOTAL RUNS : {user_runs_total} \n")
            comp_ball_count += 1
            if user_runs_total > comp_runs_total:
                print("\n \t !!!YOU WON!!!")
                break
        else:
            print(f"\t BALL : {comp_ball}\t RUN : {user_runs}")
            print("\t \t !!!OUT!!!")
            print(f"\t TARGET : {comp_runs_total + 1} \t TOTAL RUNS : {user_runs_total}")
            if user_runs_total > comp_runs_total:
                print("\n \t !!!YOU WON!!!")
            else:
                print("\n \t COMPUTER WON :(")
            user_out = True
