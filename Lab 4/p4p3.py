# Author Conor O'Kelly
# Date 29/9/15
# Student number = 15203728

number = 1520.3738


def tax(income):
    if income <= 0:
        print "The income must be greater then zero. Please try again."
    else:
        income_1 = income * 0.6
        income_2 = income * 0.4

        first_level = income_1 * 0.135
        second_level = income_2 * 0.23

        total_tax = first_level + second_level

        total = total_tax + income

        print 'Income is', income, "tax due is", total_tax
        print "The total amount of income plus tax is", total
        print ("The total formated is %.2f" % total)

#Test 1
print "Test 1 - Less then zero amount"
tax(0)

#Test 2
print "\nTest 2 - student number amount."
tax(number)
