__Author__ = "Conor O'Kelly"

def sum_upto_input():

    number = get_input_int()

    adder = 1
    sum_ints = 0
    
    while adder <= number:
        sum_ints += adder
        
        adder += 1

    print "The sum of the ints up to and including %i is %i" % (number, sum_ints) 

def get_input_int():

    number = raw_input ("What number would you like to use \n")
    number = int(number)

    return number



# Test 1
sum_upto_input()
