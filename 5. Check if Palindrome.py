'''
**Check if Palindrome** - 
Checks if the string entered by the user 
is a palindrome. That is that it reads the 
same forwards as backwards like “racecar”
'''


def palindrome():
    user_input = input('Co chcesz: ')
    reversed_input = ''.join(reversed(user_input))
    if reversed_input == user_input:
        print('It is a palindrome')
    else:
        print('Thats not a palindrome')

def main():
    palindrome()

if __name__ == '__main__':
    main()
