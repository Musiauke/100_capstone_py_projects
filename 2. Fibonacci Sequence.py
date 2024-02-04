'''
**Fibonacci Sequence** - Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.
'''

fibonacci_list = [0,1]

n = int(input("Input your n which will allow you to see required part of Fibonacci sequence: "))

for x in range(n -2):
    next_element = fibonacci_list[-1] + fibonacci_list[-2]
    fibonacci_list.append(next_element)

print(fibonacci_list)
