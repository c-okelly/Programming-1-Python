__Author__ = "Conor O'Kelly"

def prompt_numbers():
    print "Hello, can you please enter three int numbers"
    no_1 = raw_input("Enter number one \n")
    no_2 = raw_input("Enter number two \n")
    no_3 = raw_input("Enter number three \n")

    no_1 = int(no_1)
    no_2 = int(no_2)
    no_3 = int(no_3)

    numbers = [no_1, no_2, no_3]

    odd_numbers = []
    
    for i in numbers:
        if (i % 2) == 1:
            odd_numbers.append(i)

    if len(odd_numbers) == 0:
        print "There are no odd numbers"
    else:
        odd_numbers.sort(reverse=True)
        print "The largest odd number is", odd_numbers[0]


# Test 1
prompt_numbers()
