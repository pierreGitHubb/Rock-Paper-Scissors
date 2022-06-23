print("Hi, thank for playing at the Rock, Paper, Scissors game")

def win():
    print("You have win at this game")

def lose():
    print("You have lose at this game")


choose = input("Choose: Rock, Paper or Scissors?: ")


def Rock():
    if choose == "Rock":
        computer_choose = "Paper"

        if choose == "Rock" and computer_choose == "Paper":
            lose()
            print("The PC have choosed this: ", computer_choose)

def Paper():
    if choose == "Paper":
        computer_choose = "Scissors"

        if choose == "Paper" and computer_choose == "Scissors":
            lose()
            print("The PC have choosed this: ", computer_choose)

def Scissors():
    if choose == "Scissors":
        computer_choose = "Rock"

        if choose == "Scissors" and computer_choose == "Rock":
            lose()
            print("The PC have choosed this: ", computer_choose)


Rock()
Paper()
Scissors()