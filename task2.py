"""
Create a program to play a number guessing game
There should be a function:
title()
displays instructions and how to play

game()
plays the game

This will be silimar to something you have already done, but in this task you 
are breaking the code up into different sections to make each a function.
"""
def title():
    print("Welcome to the number guessing game!")
    print("In this game, you must guess the number i am thinking of.")
    print("The number cannot be above 10.")
    print("To play the game, you must press a number key on your [bold]keybaord[/bold] to guess a number.")
    print("Then, you must press the [bold]ENTER[/bold] key to present your guess,")
    print("and I'll tell you if you got it right or wrong.")
    print("Oh, do not type out the numbers using the letter keys! just press the number keys.")

def game():
    guess = int("Very well, please present your guess now.")
    