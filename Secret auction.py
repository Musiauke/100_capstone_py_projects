import os

def clear_screen():
    os_system = os.name
    if os_system == 'posix': 
        os.system('clear')



logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("Welcome to the secret auction program")

bidders = []

def add_new_bidder(id, amount):
    new_bidder = {}
    new_bidder["name"] = id
    new_bidder["bid"] = amount
    bidders.append(new_bidder)

while True:
    name = input("What is the name of bidder? ")
    clear_screen()
    bid = input("What is the bid in $? ")
    clear_screen()
    add_new_bidder(name, bid)

    proceed = input("Are there any other bidders? Type 'yes' or 'no' ").lower()
    if proceed == 'yes':
        pass
    else:
        max_bid = max([bidder["name"] for bidder in bidders])
        print(f"The winner is {max_bid}")
        break
        
