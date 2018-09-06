hole = 1
while hole < 19:
    par = int(input("Par of hole {}: ".format(hole)))
    score = int(input("Score on hole {}: ".format(hole)))
    if score == par:
        print("par")
    elif score == par + 1:
        print("bogey")
    elif score == par + 2:
        print("double bogey")
    elif score == par + 3:
        print("triple bogey")
    elif score > par + 3:
        print("bad hole")
    elif score == par - 1:
        print("birdie")
    elif score == par - 2:
        print("eagle")
    elif score == par - 3:
        print("albatross")
    elif score < par - 3:
        print("invalid score")
    hole += 1
    