# Author Conor O'Kelly
# Date 29/9/15
# Student number = 15203728

number = 1520.3738

def conveter(amount, conversion_rate):
    if amount <= 0:
        print "The amount must be greater then zero. Please try again"
    else:
        new_amount = amount * conversion_rate
        print new_amount



# convetering pounds to euro
# 1 pound is equal to 1.35 euro

#Test 1
print "Test 1 - Zero amount"
conveter(0, 1.35)

#Test 2
print "\nTest 2 - student number amount. Using poounds to euros."
conveter(number, 1.35)
