__Author__ = "Conor O'Kelly"



def multiplication_table():

    input_number = get_input_int()
    number_1 = 1
    number_2 = 1

    while number_1 <= input_number:
        
        while number_2 <= input_number:
            
            result = number_1 * number_2
            
            print result 

            number_2 += 1
            
        number_2 = 1 
        number_1 += 1
    

def get_input_int():

    number = raw_input ("What number would you like to check \n")
    number = int(number)

    return number



# Test 1
multiplication_table()
