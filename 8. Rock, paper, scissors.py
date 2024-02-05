# Rock, paper, scissors

import random

player_score = 0

computer_score = 0

rules = {
    'Scissors': 'Paper',
    'Paper': 'Rock',
    'Rock': 'Scissors'
}


def how_many_rounds(): # Here user choose how many round he wants to take 1 or 3
        
    try:

        num_rounds = int(input("We are going to play paper, rock, scissors. How many rounds would like to play 1 or 3? "))

        if num_rounds == 1:
            print("We are going to play one round" )
            one_round()
        elif num_rounds == 3:
            print("We are going to play three round" )
            three_rounds()
        else:
            print("Wrong input, try again")
    except ValueError:
        print("Wrong input, try again. Choose 1 or 3.")


def player_choice():

    global player_score, computer_score
    
    while True:
        player_move = input("What is your move? ").capitalize()
        if player_move in rules:
            break
        print("Invalid move. Please choose Scissors, Rock, or Paper.")
        
    computer_move = random.choice(list(rules.keys()))
    
    print(f"Computer chose {computer_move}")
    
    if player_move == computer_move:
        print("It's a draw!")
    elif rules[player_move] == computer_move:
        print("You won!")
        player_score += 1
    else:
        print("You lose!")
        computer_score += 1


def check_if_win_one_round():
    if player_score > computer_score:
        print("You won")
        return "won"
    elif player_score < computer_score:
        print("You lost")
        return "lost"
    return "continue"

def check_if_win_three_rounds():
    if player_score == 3:
        print("You won")
        return "won"
    elif computer_score == 3:
        print("You lost")
        return "lost"
    return "continue"

def one_round():
    while True:
        player_choice()
        result = check_if_win_one_round()
        if result == "won" or result == "lost":
            break

def three_rounds():
    while True:
        player_choice()
        result = check_if_win_three_rounds()
        if result == "won" or result == "lost":
            break


def display_final_score():
    print(f"Final score - Player: {player_score}, Computer: {computer_score}")
    if player_score > computer_score:
        print("Congratulations! You are the overall winner!")
    elif player_score < computer_score:
        print("Oh no! The computer won this time. Better luck next time!")
    else:
        print("It's a tie!")

def main():
    how_many_rounds()
    display_final_score()

main()
