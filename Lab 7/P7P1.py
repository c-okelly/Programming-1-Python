__Author__ = "Conor O'Kelly"

def check_year():

    year = raw_input("Please enter a year\n")
    year = int(year)

    if year >= 0:
        if (year % 4) == 0 and (year % 100) != 0:
            print "The year is a leap year"
        else:
            print "The year is not a leap yaer"
    else:
        print "The year must be greater then 1"
        

# Test 1
check_year()
