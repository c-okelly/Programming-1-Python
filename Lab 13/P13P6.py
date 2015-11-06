__author__ = 'conor'


"""
Program

def checker_posotive();

    number = user_input

    if int positive:
        factorial(number)
    else:
        print " number not positive"

def get_factorial(number):
    result = 0

    if number < 1:
        retun 1
    else:
        result

    return result

"""

def main():
    number = get_input()

    check_positive(number)

def get_factorial(number):

    if number < 1:
        return 1
    else:
        print("The result is multipled by %0.2f" % (number))
        return (number * get_factorial(number - 1))


def check_positive(number):
    if number >= 0:
        result = get_factorial(number)
        print("The factorial of %0.2f is %0.2f" % (number, result))
    else:
        print("The number entered is less then 0")

def get_input(): # Function to get input number
    number = float(raw_input("Please enter a number (float) \n"))
    return number


main()