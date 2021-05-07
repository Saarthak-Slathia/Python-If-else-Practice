'''
Problems:
Write the conditional expression for the following:-
    1. Create a variable "a" whose value depends on the input of the user and develop a logic that if the value of a is less than 10, then set the value of variable "b" as 20 and print it, or else set the value of b as 40 and print it. [Print the values using formated ("f") strings.]

    2. Create a variable "time" whose value depends on the time entered in the form of integers inputed by the user and create a logic that checks:
        if the value of "time" is less than 12, print "Good Morning"
        if the value of "time" is more than 24, print "Invalid Input !!!"
        else, print "Good Afternoon"

    3. Create a variable "marks" which takes input from the user in form of integers of their marks and develop a logic that:
        if the value of marks is equal-to or greater than 75, print True.
        if the value of marks at the same time is greater than 100, print "Invalid Input !".
        else, print False. 
'''

# Problem-1

a = int(input("Enter the value in numbers: ")) # Defining the variable a.

# Logic of the program
if a < 10: # Condition
    b = 20
    print(f"The value of b is {b}")

else: # If none of the condition matches, statements to be executed.
    b = 40
    print(f"The value of b is {b}")

##########################################################################################

# Problem-2

# Defining the variable "time"
time = int(input("Enter the hours passed today in the form of numbers: "))

# Developing the logic
if time < 12: # Condition-1
    print("Good Morning")

elif time > 24: # Condition-2
    print("Invalid Input !!!")

else: # No condition matches.
    print("Good Afternoon")

##########################################################################################

# Problem-3

# Variable Marks
marks = int(input("Enter your marks in form of numbers between 1-100: "))

# Logic of the Program
if marks >= 70 and marks <= 100: # Condition-1
    print(True)

elif marks > 100: # Condition-2
    print("Invalid Input")

else: # Condition-3
    print(False)


##########################################################################################

"""
Here comes a challenge:
1. Rewrite the following code snippet in just 1 line 😱: (Hint: You can declare the variable in another line)
    x = 4
    y = 4.00
    
    if x == y:
        print("The value of x and y is equal.")

    else:
        print("The value of x and y is not equal.")

"""

# Challenge Solution.
x, y = 4, 4.00
# print(x) # Just to check if the values of the variable are defined properly

print("The value of x and y is equal") if x == y else print("The value of x and y is equal")
# This is the syntax for writing he if-else conditional statements in 1 line.



# 😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀😀 #
