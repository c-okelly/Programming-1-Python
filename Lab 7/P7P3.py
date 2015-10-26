__Author__ = "Conor O'Kelly"

def counter():

    count = 0
    
    while count < 51:
        count_square = (count ** 2)

        print "The number is", count, "and its square is", count_square

        count += 1


# Test 1
counter()
