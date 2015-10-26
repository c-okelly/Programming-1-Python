__Author__ = "Conor O'Kelly"

def factorial_calculator():

    number = 1
    
    while number >= 0:

        number = get_input_int()
        
        if number >= 0:
            result = factorial(number)

            print "The factorial of %i is %i" % (number, result)

    print "The program has ended due to a negative number"

def factorial(number):

    number_1 = number
    result = 1
    

    for i in range(1, number_1 + 1):
        result = result * i
        
    return result

def get_input_int():

    number = raw_input ("What number would you like to use \n")
    number = int(number)

    return number

#Test 1
factorial_calculator()
