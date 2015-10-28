__author__ = "Conor O'Kelly"
"""
pseudocode



"""

def main():


    number = get_input()

    if number <= 0:
        print "The number is less then or equal to 0. Program ending"
    elif number == 1:
        print "The series is 1"
    else:
        fib_series = [1,1]
        count = 2


        while count < number:
            # Reverse list
            fib_reverse = fib_series[::-1]

            next_in_series = fib_reverse[0] + fib_reverse[1]
            fib_series.append(next_in_series)
            # print fib_series

            count += 1

        print "The series for", number, "is", fib_series




def get_input():
    number = int(raw_input("Please enter a number (int) \n"))
    return number

#main()

list_1 = [1,2,3]

x = list(reversed(list_1))

print x
