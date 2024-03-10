import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

dealer_hand = []
player_hand = []

def draw(who):
    who.append(random.choice(cards))

def points_sum(hand):
    total = sum(hand)
    # Ajust for aces
    num_aces = hand.count(11)
    while total > 21 and num_aces:
        total -= 10
        num_aces -= 1
    return total

def round():
    global dealer_hand, player_hand
    
    if points_sum(player_hand) < 21:
        hit_or_stand = ''
        while hit_or_stand not in ['d', 's']:
            hit_or_stand = input("Would you like to draw (d) or stand (s)? ").lower()
            if hit_or_stand not in ['d', 's']:
                print("Invalid input, please choose 'd' to draw or 's' to stand.")
        
        if hit_or_stand == 's':
            while points_sum(dealer_hand) < 17:
                draw(dealer_hand)
            print(f"Dealer's hand: {dealer_hand}")
            print(f"Player's hand: {player_hand}")

            if points_sum(player_hand) > 21:
                print("You lost! ")
            elif points_sum(dealer_hand) > 21 or points_sum(player_hand) > points_sum(dealer_hand):
                print("You won! ")
            elif points_sum(player_hand) < points_sum(dealer_hand):
                print("You lost! ")
            else:
                print("It's a tie! ")
        elif hit_or_stand == 'd':
            draw(player_hand)
            print(f"Dealer's hand: {dealer_hand[0]}")
            print(f"Player's hand: {player_hand}")
            round()  
    else:
        print("You lost! ")

def game():
    global dealer_hand, player_hand  
    
    dealer_hand.clear()  
    player_hand.clear()
    
    for i in range(2):  
        draw(dealer_hand)
        draw(player_hand)
     
    print(f"Dealer's hand: {dealer_hand[0]}")
    print(f"Player's hand: {player_hand}")  
    
    round()


game()
