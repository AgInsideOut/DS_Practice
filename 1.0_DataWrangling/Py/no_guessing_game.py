""" As you might know, Python only provides two kinds of loops: for and while. 
Knowing how to write and use them will serve you well throughout your Python career. 
The fact that nearly every type of data knows how to work inside of a for loop makes 
such loops common and useful. If you're working with database records, elements in an 
XML file, or the results from searching for text using regular expressions, you'll be 
using for loops quite a bit.

For this exercise :
- Write a function (guessing_game) that takes no arguments.
- When run, the function chooses a random integer between 0 and 100 (inclusive).
- Then ask the user to guess what number has been chosen.
- Each time the user enters a guess, the program indicates one of the following:
        Too high
        Too low
        Just right
- If the user guesses correctly, the program exits. Otherwise, the user is asked to try again.

* The program only exits after the user guesses correctly.
* We'll also be prompting the user to enter text with the input function. We'll actually be using 
input quite a bit in this book to ask the user to tell us something. 
* The function takes a single string as an argument, which is displayed to the user. The function then returns the string 
containing whatever the user entered; for example:

        ``` name = input('Enter your name: ')
        print(f'Hello, {name}!') ```
        
* NOTE If the user simply presses Enter when presented with the input prompt, the value returned 
by input is an empty string, not None. Indeed, the return value from input will always be a string, 
regardless of what the user entered. """

# SOLUTION

import random

def guessing_game():
    r_num = random.randint(0, 100)
    
    while True:                                              # Start an infinite loop that continues until a correct guess is made.
        u_num = int(input("What number has been chosen?\t")) # Ask the user for input inside the loop so they can take multiple guesses.
        
        if u_num > r_num:
            print("Too high\t")
        elif u_num < r_num:
            print("Too low\t")
        else:
            print("Just right!")
            print(f"The number is {r_num}!")
            break                                           # Exit the loop when the correct number is guessed.

guessing_game()
