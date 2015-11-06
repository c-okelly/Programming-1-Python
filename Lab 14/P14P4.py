__author__ = 'conor'

# Program from class
# edited to give out number pairs
# Program to illustrate the use of the else statement on a for loop
# Search for prime numbers in a range of integers
# Look for prime numbers in a range of integers


def main():
    for number in range(2, 20):
        # List of factors for a particular number
        factor_list = []
        for i in range(2, number):

            if number % i == 0:
                factor = "%i * %i" % (number/i, i)
                #print(number, factor)
                factor_list.append(factor)

        if len(factor_list) == 0:
            # loop fell through without finding a factor
            print number, "is a prime number"

        else:
            print("The factors for %i are %s") % (number, factor_list)

    print "Finished!"

main()
