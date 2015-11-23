__author__ = 'conor'
"""
Find divisor of one number

test greater then 0

if not create tuple with 1 and number as divisors

For i in range 2 to half number plus one.

Test that it can be divided if can create new tuple with combination of both

"""


# Find the common deivsor of both numbers
def find_divisors(number_1):


    divisors_found = (1,number_1)
    # Set starting tuple equal to 1. Include smaller number in divisor
    if number_1 <= 0:
        print "The number %i is less  or equal to zero. Exiting program."
    elif number_1 > 0:

        for i in range(2,(number_1/2 + 1)):
            if (number_1 % i) == 0:
                divisors_found += (i,)

    print("The divisors of %i are %s" % (number_1, divisors_found) )
    return divisors_found

def get_input():
    number = int(raw_input("Please enter a number for the function (int) \n"))
    return number



if __name__ == '__main__':
    number = get_input()

    find_divisors(number)