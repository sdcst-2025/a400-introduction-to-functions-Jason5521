"""
Create a program with 3 function definitions:
function A prints the message "Hello"
function B prints the message "How are you"
function C prints the message "Hi"

Ask the user to enter a letter from A to C
Execute the function of the letter they use.
"""

def A():
    print("Hello")

def B():
    print("How are you")

def C():
    print("hi")


# ask the user to enter a letter A - C
# check the letter to see what it is
# if A, then A()
# if B, then B()
# if C, then C()

Letter = input("Enter a letter from A to C: ")
if Letter == "A":
    A()
elif Letter == "B":
    B()
elif Letter == "C":
    C()