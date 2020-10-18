import random

rungame = True

while rungame == True:
    cpu = random.randint(1, 3)
    print("NEW GAME")
    print("-----------------")
    user = int(input("1 - Rock\n2 - Paper\n3 - Scissors\n-Player input: "))
    print("-----------------")

    print(f"CPU:{cpu}")
    print(f"USER:{user}")


    # cpu response: rock
    if cpu == 1 and user == 1:
        print("Tie")
    if cpu == 1 and user == 2:
        print("Player Wins")
    if cpu == 1 and user == 3:
        print("Player Loses")


    # cpu response: paper
    if cpu == 2 and user == 1:
        print("Player Loses")
    if cpu == 2 and user == 2:
        print("Tie")
    if cpu == 2 and user == 3:
        print("Player Wins")


    # cpu response: scissors
    if cpu == 3 and user == 1:
        print("Player Wins")
    if cpu == 3 and user == 2:
        print("Player Loses")
    if cpu == 3 and user == 3:
        print("Tie")

    run = input("Would you like to play again? [Yes/No]: ")
    if run == "Yes":
        rungame = True
    elif run == "No":
        rungame = False
    else:
        print("doh")
    print("-----------------")
