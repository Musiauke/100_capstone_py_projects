'''
**Reverse a String** - Enter a string and the program
 will reverse it and print it out.
'''


def reverse_string():
    user_input = input('Enter a string you want to reverse: ')
    reversed_string = ''.join(reversed(user_input))
    return (reversed_string)


def main():
    print(reverse_string())

if __name__ == '__main__':
    main()

