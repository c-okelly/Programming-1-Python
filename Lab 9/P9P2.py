__Author__ = "Conor O'Kelly"

def add_number_list():


    number = 0
    number_list = []
    
    print "Please enter a series of numbers"
    
    while number >= 0:
        number = get_input_int()
        if number >0:
            number_list.append(number)
        sum_list = 0

        for i in number_list:
            sum_list += i

        print "The sum of all numbers is now %i" % (sum_list)
    print "The program has now ended"
    

def get_input_int():

    number = raw_input ("Please give me a number \n")
    number = int(number)

    return number


# Test 1

add_number_list()
