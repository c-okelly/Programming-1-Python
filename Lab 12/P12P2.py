__author__ = "Conor O'Kelly"


"""
pseudocode

main()
    get user input

    if user input > 0:
        call fib_series function
    else:
        print error messages

fib_series()
    calculate fib_series using old formula

"""

def main():

    user_input = get_input()

    if user_input >0:
        fib_series(user_input)
    else:
        print "The number that has been entered is equal to 0 or negative"


def fib_series(number_of_terms):

    if number_of_terms == 1:
        print "The series is [1]"
    else:
        fib_series = [1,1]
        # Start count at 2 => first two number already in series
        count = 2
        while count < number_of_terms:
            # Reverse list
            fib_reverse = fib_series[::-1]

            # Added next item to lsit
            fib_series.append(fib_reverse[0] + fib_reverse[1])

            # Increase count
            count += 1

        print "The series for %i is %s" % (number_of_terms, fib_series)


def get_input():
    number = int(raw_input("Please enter a number (int) \n"))
    return number

main()