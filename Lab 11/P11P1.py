__author__ = "Conor O'Kelly"


"""
pseudocode

set the result equal to 1

print error if number below 0
if number is greater then or equal to 0
    Run factorial function to find result and set factorial to new number only if number is greater then 0
    if number = 0 do no run while loop
    Factorial is already set at 1


Print result (if number is 0 factorial is already set)

"""

number = int(raw_input("Enter the number for which you wish to calculate the factorial (an int >= 0): "))

factorial = 1

if number < 0:
    print 'Error: Number entered was less than 0.'
elif number >= 0:
    count = 1

    while count <= number:
        factorial *= count
        count += 1

    print "Factorial of", number, "is", factorial