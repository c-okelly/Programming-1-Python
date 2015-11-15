__author__ = 'conor'

"""
Psuedocode

def series(number):
    if number == 1:
        return 2
    else:
        print "doing number x"
        return number - series(number - 1)

def get_input():
    get input

def get_series():

    check above 0

    if yes run function

    elif exit

"""

def series(number):
    if number == 1:
        print("Currently calculating for number 1. Last one \n")
        return 2
    else:
        print ("Currently calculating for number %i" % (number))
        return (number + series((number-1)))


def get_input():
    number = int(raw_input("Please enter a number for the function (int) \n"))
    return number

def get_series():
    number = get_input()

    while number >= 1:
        print ("The result is %i \n" % (series(number)))
        number = get_input()

    else:
        print("The number is below 1. Exiting")
    return


if __name__ == '__main__':
    get_series()