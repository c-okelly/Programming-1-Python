__author__ = 'conor'

"""

def find_if_perfect_number(number):
    find all integer

    if all integer add = number
        return number
    else:
        return

def series():


def get_input():

    x = int(raw_input("Enter limit of perfect number search"))

"""

def find_if_perfect_number(number):

    #Find integers
    factors_list = [1]

    for i in range(2,number):
        if (number % i) == 0:
            factors_list.append(i)

    # Find sum of list
    sum_list = sum(factors_list)

    # Return if equal
    if sum_list == number:
        return number


def run_for_range():

    number = get_input()

    result_list = []

    for i in range (2,number+1):
        result = find_if_perfect_number(i)


        if result != None: # Ony add result for list if number returned. Exclude None value
            result_list.append(result)

    print(result_list)

def get_input():
    number = int(raw_input("Please limit of perfect number search (int) \n"))
    return number


if __name__ == '__main__':
    run_for_range()


