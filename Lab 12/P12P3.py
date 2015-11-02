__author__ = "Conor O'Kelly"


"""
pseudocode
main()
    prompts for number and tolerance

    if number greater then 0 entered:
        call calculate_root()
        if result found
            print result
        if result not found
            print message
    else:
        print error message



calculate_root()
    using algorithm from class
    Progam attempts to find root with tolerance
    if root found:
        returns array with results and Ture boolean
    if not found:
        returns array with result and False boolean

"""

def main():

    print "Please enter the number you want to find the square root of"
    number = get_input()
    #print("Please enter the tolerance form the program")
    #tolerance = get_input()
    tolerance = 0.01

    if number > 0:
        result = calculate_root(number, tolerance)

        if result[1] == True:
            print("The approx sqaure root of %i is %i" % (number, result[0]))

        elif result[1] == False:
            print("The program was not able to find a square root.")

    else:
        print("The number entered is 0 or negative")

def calculate_root(number, tolerance):

    # Code from class

    worked = False

    step = tolerance * 2
    no_of_guesses = 0

    root = 0.0

    while abs(number - (root ** 2)) >= tolerance and root ** 2 <= number:
        root += step

    if abs(number - root ** 2) < tolerance:
        worked = True
        #print(root)
        return root, worked
    else:
        #print("problem")
        return root, worked

def get_input():
    number = float(raw_input("Please enter a number (int) \n"))
    return number


main()
