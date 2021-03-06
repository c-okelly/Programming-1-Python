__author__ = 'conor'


"""
Program to print out the largest of two numbers entered by the user
Uses two functions: max and print_max
"""

def get_input(): # Function to get input number
    number = float(raw_input("Please enter a number (float) \n"))
    return number

def print_max(): #Function that prints out the largest of two numbers
    #Uses the function max to find the largest
    def max(a, b): #Function that returns the largest of its two arguments
        if a > b:
            return a
        else:
            return b

    # Prompt the user for two numbers

    number1 = get_input()
    number2 = get_input()


    print("The largest of %0.2f and %0.2f is %0.2f" % (number1, number2, max(number1,number2)))
    print("Finished")


print print_max

