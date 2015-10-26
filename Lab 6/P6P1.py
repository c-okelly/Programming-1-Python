__Author__ = "Conor O'Kelly"

def prompt_numbers():
    print "Hello, can you please enter two numbers"
    no_1 = raw_input("Enter number one \n")
    no_2 = raw_input("Enter number two \n")

##    print no_1, no_2
    no_1 = int(no_1)
    no_2 = int(no_2)

    sum_no =  no_1 + no_2 
    print "First number", no_1, "plus second number", no_2, "is equal to", sum_no


# Test 1 
prompt_numbers()
