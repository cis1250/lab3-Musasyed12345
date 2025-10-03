#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

print('User input: ', end='')
amount = input()

while not amount.isdigit() or int(amount) < 0:
    print('Expected output: Please enter a positive integer.')
    print()
    print('User input: ', end='')
    amount = input()

amount = int(amount)
print('Expected output: ', end='')
num_one = 0
num_two = 1
for i in range(amount):
    print(num_one, end='')
    if i < amount - 1:
        print(' ', end='')
    temp = num_one
    num_one = num_two
   num_two = temp + num_two

print() 



