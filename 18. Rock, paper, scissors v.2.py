import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

choices = ["r","p","s"]

win_scenarios = {'r':'s',
                 's':'p',
                 'p':'r'
                  }

user_choice = input("What you wannt to pick? r, p or s?").lower()
computer_choice = random.choice(choices)

print(f"Your choice is: {user_choice}\nComputer: {computer_choice}")

if user_choice == 'r':
    print(rock)
elif user_choice =='s':
    print(scissors)
else:
    print(paper)

if computer_choice == 'r':
    print(rock)
elif computer_choice =='s':
    print(scissors)
else:
    print(paper)

if user_choice == computer_choice:
    print("It's a tie!")
elif win_scenarios[user_choice] == computer_choice:
    print("You won")
else:
    print("You lose")
