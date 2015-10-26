#__Author__ = "Conor O'Kelly"


def number_checker(number):
    if number < 0:
        print "The number is negative \n"
    elif number == 0:
        print "The number is eqaul to 0 \n"
    elif number <= 20:
        print "The number is between 0 and 20 \n"
    elif number <= 40:
        print "The number is between 20 and 40 \n"
    elif number <= 60:
        print "The number is between 40 and 60 \n"
    elif number <= 80:
        print "The number is between 60 and 80 \n"
    elif number <= 100:
        print "The number si between 80 and 100 \n"
    else:
        print "The number is greater the 100 \n"

        
        
# Test 1 -> number negative
print "Test 1 => nubmer equal to -3." 
number_checker(-3)
       
# Test 2 -> number 0
print "Test 2 => nubmer equal to 0" 
number_checker(0)

# Test 3 -> number 18
print "Test 3 => nubmer equal to 18" 
number_checker(18)

# Test 4 -> number 38
print "Test 2 => nubmer equal to 38" 
number_checker(38)

# Test 5 -> number 58
print "Test 2 => nubmer equal to 58" 
number_checker(58)

# Test 6 -> number 79
print "Test 2 => nubmer equal to 79" 
number_checker(79)

# Test 7 -> number 90
print "Test 2 => nubmer equal to 90" 
number_checker(90)

# Test 8 -> number 190
print "Test 2 => nubmer equal to 190" 
number_checker(190)

