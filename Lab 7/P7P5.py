__Author__ = "Conor O'Kelly"

def adder():

    count = 0
    sum_numbers = 0 
    
    for i in range(0,10001):
        if (i % 3) == 0:
##            print count
            sum_numbers += count
        elif (i % 5) == 0:
            sum_numbers += count
##            print count

        count += 1
        
    print sum_numbers
        

adder()
