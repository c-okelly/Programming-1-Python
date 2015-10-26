__Author__ = "Conor O'Kelly"

def ask_name():
    
    name = raw_input("Please enter you name \n")
    name = name.lower()

    if name == "conor okelly":
        print "That is a cool name"
    elif name == "mickey mouse" or name == "spongebob squarepants":
        print "I don't think that is your name"
    else:
        print "That is a nice name"
        
    

# Test 1
ask_name()
