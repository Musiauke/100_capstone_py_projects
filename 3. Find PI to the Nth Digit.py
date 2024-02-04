'''
**Find PI to the Nth Digit** - Enter a number and have the program generate &pi; (pi) up to that many decimal places. Keep a limit to how far the program will go.
'''

import math

pi = math.pi


while True:
    try:
        user_digits = int(input('How much you want to see? '))
        if user_digits < 500:
            print(f'Your pi seen to {user_digits} look like: {pi:.{user_digits}f}')
            break
        else: 
            print('The maximum input is 500')
    except ValueError:
        print('Invalid input, try again')
        
