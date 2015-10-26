__Author__ = "Conor O'Kelly"

def counter():

    count = 0
    sum_numbers = 0
    
    while count < 5001:

        sum_numbers += count
        
        count += 1

    print sum_numbers


# Test 1
counter()
