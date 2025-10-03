#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.

def fibonacci_sequence():
    """Calculates and prints the Fibonacci sequence up to a specified number of terms."""

    while True:
        user_input = input("Enter how many terms of the Fibonacci sequence you want: ")

        
        if user_input.isdigit():
            num_terms = int(user_input)

            if num_terms > 0:
             break
 else:
       print("Please enter a positive integer greater than 0.")
 else:
       print("Please enter digits only (positive integer).")

    a, b = 0, 1
   
    if num_terms == 1:
        print(a)
    elif numterms >= 2:
        print(a, end=" ")
        print(b, end=" ")

        for  in range(2, num_terms):
            next_term = a + b
            print(next_term, end=" ")
            a, b = b, next_term

    print()  

