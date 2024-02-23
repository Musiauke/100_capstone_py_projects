line1 = [" ", " ", " "]
line2 = [" ", " ", " "]
line3 = [" ", " ", " "]

map = [line1, line2, line3]
position = input("Where you want to put your treasure? Choose row from A to C and then line from 1 do 3: ")

letter = position[0].lower()

abc = ['a','b','c']

letter_index = abc.index(letter)
number_index = int(position[1]) - 1
map[letter_index][number_index] = "X"


print(f"{line1}\n{line2}\n{line3}")
