__author__ = 'conor'

"""
Takes in use string

turn string into list by seperating on space

checks for word type in list

if cat or dog add 1 to each counter

compares results at the end

"""

def take_string():
    words = raw_input("Please give me a string of words. Seperated by a space\n")
    return words

def check_cat_dog():
    words = take_string()
    list_words = words.split()

    number_cats = 0
    number_dogs= 0

    for i in list_words:
        if i.lower() == 'cat':
            number_cats += 1
        elif i.lower() == 'dog':
            number_dogs += 1

    if number_cats == number_dogs:
        print("There words cat and dog appeared %i times. An equal number of times" % (number_dogs))
    else:
        print("The words cat appeared %i times and dog appeared %i times" % (number_cats, number_dogs))

if __name__ == '__main__':
    check_cat_dog()
