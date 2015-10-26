__Author__ = "Conor O'Kelly"


def find_range():

    number = get_input_int()
    
    #Numbers in range of 0-20, 21-40, etc
    range_0 = 0 #0-20
    range_1 = 0 #21-40
    range_2 = 0 #41-60
    range_3 = 0 #61-80
    range_4 = 0 #81-100
    range_5 = 0 #101 plus
    
    while number > 0:
        if number <= 20 and number > 0:
            print "The number is between 0 and 20"
            range_0 += 1
        elif number <= 40:
            print "The number is between 21 and 40"
            range_1 += 1
        elif number <= 60:
            print "The number is between 41 and 60"
            range_2 += 1
        elif number <= 80:
            print "The number is between 61 and 80"
            range_3 += 1
        elif number <= 100:
            print "The number is between 81 and 100"
            range_4 += 1
        elif number > 100:
            print "The number is greater then 100"
            range_5 += 1

        number = get_input_int()
        
    print "Number in the following ranges where input \n"
    print "In 0-20 => %i, 21-40 => %i, 41-60  => %i, 61-80  => %i, 81-100  => %i, 100 plus => %i \n" % (range_0,range_1,range_2,range_3,range_4,range_5)
    print "The program has now ended"

def get_input_int():

    number = raw_input ("What number would you like to check \n")
    number = int(number)

    return number

# Test 1
find_range()
