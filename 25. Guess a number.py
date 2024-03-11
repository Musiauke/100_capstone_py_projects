import random

def guessing(diff):
    lives = 0
    lives += int(diff)
    random_num = random.randint(1,100) 
    while lives > 0:
      guess = int(input("Input your guess: "))
      if guess == random_num:
          print("You guessed! ")
          return
      else:
          lives -= 1
          if lives > 0:
            if guess > random_num:
               direction = "lower"
            else:
               direction = "higer"

            print((f"Try again, you have {lives} left, try {direction} number: "))
          else:
             print("You lost! ")
             return


def game():
  question = input("Which level of difficuly would you like to choose? Easy (e) or hard (h), type the letter: ")
  if question == 'h':
      guessing(5)
  elif question =='e':
      guessing(10)
  else:
      print("Invalid input, try again ")
      game()


print("Welcome to guess a number between 1-100 game! ")
game()
