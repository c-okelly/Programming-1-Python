#__Author__ = "Conor O'Kelly"

def int_checker(number):
    if number < 0:
        print "The number is negative."
    else:
        print "The number is greater then or equal to zero."

        
# Test 1 -> number less then zero
print "Test 1 => nubmer equal to -3"
int_checker(-3)

# Test 2 -> number greater then zero
print "Test 2 => nubmer equal to 4"
int_checker(4)
