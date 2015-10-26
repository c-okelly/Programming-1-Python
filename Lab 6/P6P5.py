__Author__ = "Conor O'Kelly"

def check_password():
    count = 0
    correct_password = "code"
    password_correct = False

    while count != 3 and password_correct == False:
        password = raw_input("Please enter the password \n")
        password = password.lower()
        
        if password == correct_password:
            print "That is the correct password"
            password_correct = True
        else:
            count += 1
            print "Attempt nmuber", count, "out of 3 \n"

    if count == 3:
        print "Too many wrong attemps. Acess denied. Program quiting"
    else:
        print "You have successfully logged in"
        

# Test 1

print "Password is Code. It is not case sensitive\n\n "
check_password()
