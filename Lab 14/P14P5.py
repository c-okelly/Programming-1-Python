__author__ = 'conor'

"""
def fib_number(number):
    if number 1 or 2:
        return 1
    else:
        return fib_number(number-1) + fib_number(number-2)

def make_list(number):
    list = []

    for i in range(1,number+1)
        list.append(fib_number(i))

def get_input():
    get user input

def main():
    bring all function together


"""

def fib_number(number):

    if number == 1 or number ==2:
        return 1
    else:
        return fib_number(number-1) + fib_number(number-2)

def make_list(number):
    list = []

    for i in range(1,number+1):
        list.append(fib_number(i))
        print("The next number in the series was %i and was added to the Fibonacci list" % (fib_number(i)))

    return list

def get_input():
    number = int(raw_input("Please enter a number (int) \n"))
    return number

def main():

    number = get_input()

    while number > 0:
        list = make_list(number)
        print("The list of Fibonacci numbers to the %i place is %s" % (number, list))
        number = get_input()
    else:
        print("The number entered is 0 or below")

main()