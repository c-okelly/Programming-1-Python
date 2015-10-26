__Author__ = "Conor O'Kelly"



def multiplication_table():

    number = get_input_int()
    multiplier = 1
    
    while multiplier <= 20:

        result = number * multiplier
        
        print (result)
        multiplier += 1

def get_input_int():

    number = raw_input ("What number would you like to check \n")
    number = int(number)

    return number



# Test 1
multiplication_table()
