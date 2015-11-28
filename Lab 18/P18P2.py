__author__ = 'conor'


"""

def take_in_string():
    return a string of words

def search_in_string():
    words = take_in_string()

    count times code is found in list
"""

def search_in_string():

    sentence = string_input()
    count = sentence.count("code")

    print("The word code was found %s times" % (count) )


def string_input():
    words = raw_input("Please give sentence to search for the word 'code' in.\n")
    return words

if __name__ == '__main__':
    search_in_string()
