__author__ = "Conor O'Kelly"
"""
pseudocode

Use code from pervious program to run

Use main function to calculate series by callin fib_calculator

"""

def main():

    number = get_input()

    while number > 0:

        fib_calultor(number)

        number = get_input()

    print "The number is less then or equal to 0. Program ending"


def fib_calultor(number):

    if number == 1:
        print "The series is 1"
    else:
        fib_series = [1,1]
        # Start count at 2 => first two number already in series
        count = 2


        while count < number:
            # Reverse list
            fib_reverse = fib_series[::-1]

            # Added next item to lsit
            fib_series.append(fib_reverse[0] + fib_reverse[1])

            # Increase count
            count += 1

        print "The series for", number, "is", fib_series

def get_input():
    number = int(raw_input("Please enter a number (int) \n"))
    return number

main()