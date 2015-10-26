__Author__ = "Conor O'Kelly"

def check_devisible():


    number = get_input_int()
    
    while number >= 0:

        if (number % 2) == 0:
            print "The number is devisible perfectly by 2"

        if (number % 3) == 0:
            print "The number is devisible perfectly by 3"

        if (number % 5) == 0:
            print "The number is devisible perfectly by 5"

        if (number % 7) == 0:
            print "The number is devisible perfectly by 7"


        number = get_input_int()
        
    print "You entered a negative number. The program has now ended"
        
def get_input_int():

    number = raw_input ("What number would you like to check \n")
    number = int(number)

    return number



#Test 1
check_devisible()
