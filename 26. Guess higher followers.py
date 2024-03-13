import random
from main import data

points = 0

def formula(a_or_b, name1, occupation, origin):     
    print(f"Compare {a_or_b}: {name1}, a {occupation}, from {origin}")

def turn():
    global points

    while True:
    
        random_person_A = random.choice(data)
        random_person_B = random.choice(data)
        while random_person_B == random_person_A:
            random_person_B = random.choice(data)

        if random_person_A['follower_count'] > random_person_B['follower_count']:
            winner = "A"
        else:
            winner = "B"
        
        formula('A', random_person_A['name'], random_person_A['description'], random_person_A['country'])
        print('\nVS\n') 
        formula('B', random_person_B['name'], random_person_B['description'], random_person_B['country'])

        guessing = input("\nChoose A or B: \n").lower()

        if (guessing == 'a' and winner == 'A') or (guessing == 'b' and winner == 'B'):
            global points 
            points += 1
            print(f"You guessed! Your score is {points}")
        else: 
            print(f"You lost! Your score was {points}")
            break


def main():
    print("Welcome to higher and lower quiz game! Choose a person who you think has bigger number of followers. \n")
    turn()

main()
