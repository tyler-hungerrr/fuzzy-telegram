import random

player_wins = 0
ai_wins = 0

choices = ["rock", "paper", "scissors"]

while True:
    player_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower() #player inputs value
    if player_input == "q":
        break

    if player_input not in ["rock", "paper", "scissors"]: #valudates input
        continue

    random_num = random.randint(0, 2)
    #0 = rock, 1 = paper, 2 = scissors
    ai_pick = choices[random_num]
    print("Ai picked", ai_pick + ".")

    if player_input == "rock" and ai_pick == "scissors":
        print("You won!")
        player_wins += 1

    elif player_input == "paper" and ai_pick == "rock":
        print("You won!")
        player_wins += 1

    elif player_input == "scissors" and ai_pick == "paper":
        print("You won!")
        player_wins += 1

    elif player_input == "rock" and ai_pick == "rock":
        print("Its a draw!")

    elif player_input == "paper" and ai_pick == "paper":
        print("Its a draw!")

    elif player_input == "scissors" and ai_pick == "scissors":
        print("Its a draw!")

    else:
        print("You lost!")
        ai_wins += 1

print("You won", player_wins, "times.")
print("Ai won", ai_wins, "times.")
print("Goodbye!")
