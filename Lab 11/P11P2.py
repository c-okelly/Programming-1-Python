__author__ = "Conor O'Kelly"
"""
pseudocode

Using old formula from previous work

if the nubmer less then or equal to 0 print out error

if number is 1 print out sereis is 1

if number is greater then 1
    if number 2 print out stored fib series
    if number greater then 2
        while number in fib series list < number required
            Take last two elements of list and add them together
            (take last two by inverting list and taking first two)
            append result to list

"""

def main():


    number = get_input()

    if number <= 0:
        print "The number is less then or equal to 0. Program ending"
    elif number == 1:
        print "The series is 1"
    else:
        fib_series = [1,1]
        # Start count at 2 => first two number already in series
        count = 2


        while count < number:
            # Reverse list
            fib_reverse = fib_series[::-1]

            # Added next item to lsit
            fib_series.append(fib_reverse[0] + fib_reverse[1])

            # Increase count
            count += 1

        print "The series for", number, "is", fib_series




def get_input():
    number = int(raw_input("Please enter a number (int) \n"))
    return number

main()

