__author__ = "Conor O'Kelly"
"""
pseudocode

main()
    prompt user for input
    use range to generate number range

    for i in number_range:
        use catalan function to calculate each number
        append to list

    print results

catalan()
    result = ( (2n)! / (n+1)! * n!)

    use the factorial function to calculate the factorial of each input

find_factorial()
    resued function from old work to find factorial


"""


def main():

    # Get input and generate list of number from it
    number = get_input()
    number_range = range(1,number + 1)

    catalan_list = []

    for i in number_range:
        new_number = catalan(i)
        catalan_list.append(new_number)

    print "The list for the first %s Catalan numbers for is %s" % (number, catalan_list)


def catalan(number_input):

    if number_input == 1:
        return 1
    else:
        # Catalan number calculator
        # result = ( (2n)! / (n+1)! * n!)

        result = ( find_factorial(2*number_input) / ( find_factorial(number_input+1) * (find_factorial(number_input)) ) )

        return result


def find_factorial(input):

    count = 1
    factorial = 1

    while count <= input:
        factorial *= count
        count += 1

    #print "Factorial of", input, "is", factorial
    return factorial


def get_input():
    number = int(raw_input("Please enter a number (int) \n"))
    return number

main()
