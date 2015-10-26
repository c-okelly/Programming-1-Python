__Author__ = "Conor O'Kelly"

def factorial():

    number_1 = get_input_int()
    result = 1
    

    for i in range(1, number_1 + 1):
        result = result * i
        
    print result

def get_input_int():

    number = raw_input ("What number would you like to use \n")
    number = int(number)

    return number

#Test 1
factorial()
