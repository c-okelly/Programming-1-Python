__Author__ = "Conor O'Kelly"

def possibilites_calc():

    print "Please enter the number of possible toppings"
    number_1 = get_input_int()
    print "Please enter the number of standard pizza toppings"
    number_2 = get_input_int()

    first_line = (factorial(number_1))
    second_line = (factorial(number_2)*(factorial(number_1 - number_2)))

    result = first_line / second_line

    print result

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

possibilites_calc()
