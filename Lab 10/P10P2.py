__Author__ = "Conor O'Kelly"

"""

Get inputs to generate list


for i in list:

    While input is not equal to (integer ** 3 ) or count:

        Increser count if positve number
            count += 1
        decrement count if negative
            connt -= 1

        if (integer ** 2) == input
            Square root found
        if input == count
            square root not found
            

for each item in list perfrom find cube for number

"""
# Cube root finder function

def cube_root():

    number_list = generate_list()

    for i in number_list:
        find_cube(i) 



# Find cube root

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


# Generate list function

def generate_list():

    int_list = []
    loop_count = 1

    print "To exit enter amount as 0"
    amount = get_input_int("How many integers would you like to enter")

    if amount != 0:

        while loop_count <= amount:
            new_number = get_input_int("Please enter number %i" % (loop_count))
            int_list.append(new_number)
            loop_count += 1
    else:
        print "You entered the amount as 0. Program now exiting" 

    return int_list
    
# Get input and convert to in function

def get_input_int(phrase):

    number = raw_input ("%s \n" % (phrase))
    number = int(number)

    return number

cube_root()
