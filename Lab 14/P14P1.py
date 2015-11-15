__author__ = 'conor'

# To get system time
import time

import sys
sys.setrecursionlimit(1000000)

#  Two different way of finding the factorial

# non-recursive

def find_factorial(input):

    count = 1
    factorial = 1

    while count <= input:
        factorial *= count
        count += 1

    #print "Factorial of", input, "is", factorial
    return factorial


# recursive

def get_factorial(number):

    if number < 1:
        return 1
    else:
        return (number * get_factorial(number - 1))



def non_recursive():

    print("non-recursive")
    start_time = time.time()
    find_factorial(10000)
    print("--- %s seconds ---" % (time.time() - start_time))

def recursive():

    print("recursive")
    start_time = time.time()
    get_factorial(10000)
    print("--- %s seconds ---" % (time.time() - start_time))

def main():
    non_recursive()
    recursive()

main()

