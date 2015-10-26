#__Author__ = "Conor O'Kelly"

def int_checker(number):
    if number < 0:
        print "The number is negative."
    elif number == 0:
        print "The number is equal to zero."
    else:
        print "The number is postive."

        
# Test 1 -> number less then zero
print "Test 1 => nubmer equal to -3.3" 
int_checker(-3.3)

# Test 2 -> number equal then zero
print "Test 2 => nubmer equal to 0"
int_checker(0)

# Test 3 -> number greater then zero
print "Test 3 => nubmer equal to 4.25"
int_checker(4.25)
