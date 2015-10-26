__Author__ = "Conor O'Kelly"


"""
Pseudocode

Get input
    Convert input to int

While input is not equal to (integer ** 3 ) or count:
    Increser count if positve number
        count += 1
    decrement count if negative
        count -= 1

    if (integer ** 2) == input
        Square root found
    if input == count
        square root not found

"""

# squre root finder function

def cube_root():

    number = 1
    
    while number != 0:
        number = get_input_int()

        find_cube(number)

    print "The number entered is equal 0. Program quiting."

# Find square root

def find_cube(number):

    result = 0
    count = 0

    while number != result and number != count:

        # Order is important. Need to increase count. Then generate result for testing
        # increment count if positive / decrement if negative
        if number > 0:
            count += 1
        elif number < 0:
            count -= 1
        result = count ** 3

    # Print correct statements
    if number == result:
        print "The cube root of %i is %i" % (number, count)
    else:
        print "Could not find the cube root for the number %i" % (number)

    return count
    

# Get input and convert to in function

def get_input_int():

    number = raw_input ("Please give me a number \n")
    number = int(number)

    return number

# Test 1

cube_root()
