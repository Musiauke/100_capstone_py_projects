#Quiz game

questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the larges eggs?: ",
             "What is the most abundant gas in Earth's atmosphere?: ",
             "How many bones are in the human body?: ",
             "Which planet in the solar system is the hottest? ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
            ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
            ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
            ("A. 206", "B. 207", "C. 208", "D. 209"),
            ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A", "A", "B")

guesses = []

score = 0

question_num = 0      

def asked_question(question_num, score):
    for question in questions:
        print('---------------------')
        print(question)
        for option in options[question_num]:
            print(option)


        guess = input("Enter (A, B, C, D)").upper()
        guesses.append(guess)

        if guess == answers[question_num]:
            score += 1
            print("Correct")
        else:
            print("Incorrect")
            print(f"{answers[question_num]} is the correct answer ")


        question_num += 1
        


def Final_text():
    print('---------------------')
    print('-------Results-------')
    print('---------------------')

    print("answers: ", end=" ")
    for answer in answers:
        print(answer, end=" ")
    print()

    print("guessess: ", end=" ")
    for guess in guesses:
        print(guess, end=" ")
    print()

    print('---------------------')
    print('--------Score--------')
    print('---------------------')

    final_score = int(score / len(questions) * 100)
    print(f"---------{final_score}%---------")

def main():
    asked_question(question_num,score)
    Final_text()

if __name__ == '__main__':
    main() 
