__author__ = 'conor'


"""
Used same program that I had written last week
"""

# Find the common deivsor of both numbers
def find_divisors(number_1, number_2):

    # Set starting tuple equal to 1. Include smaller number in divisor

    if max(number_1,number_1) % min(number_1,number_2) == 0:
        divisors_found = (1,(min(number_1,number_2)))
    else:
        divisors_found = (1,)

    # Find smalles number. divide by two and add 1
    smaller_number_for_search = (min(number_1,number_2)/2) + 1

    for i in range(2, smaller_number_for_search):
        if (number_1 % i) == 0 and (number_2 % i) == 0:
            divisors_found += (i,)

    print ("The folowing divisors where found for %i and %i. %s" % (number_1, number_2, divisors_found) )
    return divisors_found


def get_input(position):
    number = int(raw_input("Please enter the %s number (int) \n" % (position)))
    return number

def run_divisor():

    print("Start of divisor program.")
    number_1 = get_input("first")
    number_2 = get_input("second")

    find_divisors(number_1, number_2)

if __name__ == '__main__':
    run_divisor()