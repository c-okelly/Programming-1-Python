__author__ = "Conor O'Kelly"


"""
pseudocode

Create main function that ask users of input

    Check if input is positive
        if positive
            Factorial function
            print results
        else
            print number is not positive

"""

def main():

    number = get_input()

    if number > 0:
        result = find_factorial(number)
        print "The factorial of %i is %i" % (number, result)
    else:
        print "the number you have entered is 0 or less"



def find_factorial(input):

    count = 1
    factorial = 1

    while count <= input:
        factorial *= count
        count += 1

    #print "Factorial of", input, "is", factorial
    return factorial

def get_input():
    number = int(raw_input("Please enter a number (int) \n"))
    return number

main()