import random

throw = random.randint(0,1)

player_input = input("Pick heads or tails? (h,t) ").lower()

if player_input == 'h':
    player_choose = 0  
else:
    player_choose = 1  

print("Let's flip a coin")

if throw == player_choose:
    print("You won")
else:
    print("You lost")

if throw == 0:
    print("It was heads.")
else:
    print("It was tails.")
