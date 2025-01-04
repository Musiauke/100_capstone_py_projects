trump_votes = 0
biden_votes = 0

def voting():
    global trump_votes, biden_votes

    vote = input("Who do you vote for: Trump or Biden? Choose T or B ")  
    if vote.lower() == 't':
        trump_votes += 1
    elif vote.lower() == 'b':
        biden_votes += 1
    else:
        print("Wrong input, try again")

if __name__ == "__main__":
    
    voting_ppl = {"Tom": 1, "Jerry": 2, "Mary": 2}
    
    while True:
        name = input("Hello what's your name? (To stop type 's'): ")
        if name.lower() == "s":
            print(f"Trump votes: {trump_votes}, Biden votes: {biden_votes}")
            break

        if name in voting_ppl:
            print(f"Hello {name}, you are on the list!")
            voting()
        else:
            print(f"Sorry {name}, you are not on the list.")


        
