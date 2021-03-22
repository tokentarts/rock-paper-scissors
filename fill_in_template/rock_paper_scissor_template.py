#!/bin/python3
from random import randint

# Your turn!
player = input('rock(r), paper(p) or scissors(s)?')
print(______, 'vs', end=' ')

# Computer's turn!
chosen = randint(1, _)

if chosen __ 1:
    computer = 'r'
elif chosen == 2:
    computer = ___
else:
    ________ = 's'
_____(computer)

# Check the result!
if player __ computer:
    print('DRAW!')
elif player == 'r' and computer == 's':
    print('____________')
elif player == 'r' ___ computer == 'p':
    print('Computer wins!')
elif ______ == 'p' and computer == 'r':
    print('Player wins!')
elif player == 'p' and computer == 's':
    _____('Computer wins!')
elif player == 's' and ________ == 'p':
    print('Player wins!')

# Can you write the last elif statement on your own?
# Lets compare player(s) and computer(r)
# Print the winner
