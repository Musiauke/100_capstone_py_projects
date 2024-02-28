import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

def main():
    display = ["_" for _ in chosen_word]
    lives = 6  

    while "_" in display and lives >= 0:
        print(" ".join(display))
        guess = input("Guess a letter: ").lower()

        if guess in chosen_word:
            for index, letter in enumerate(chosen_word):
                if letter == guess:
                    display[index] = letter
        else:
            print(stages[lives])
            lives -= 1

        if "_" not in display:
            print("You win!")
            print(" ".join(display))
            return 
        
        if lives < 0:
            print("You lose")
            print(f"The correct word was: {chosen_word}")


if __name__ == "__main__":
    main()
