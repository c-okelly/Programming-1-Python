__author__ = 'conor'



"""

def take_in_string():
    return a string of words

def search_in_string():
    words = take_in_string()

    set pattern

    use re to search the string

"""


def search_in_string():

    sentence = string_input()
    alphabet = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    count = 0

    for i in alphabet:
        count += sentence.count("co" + i + "e")

    print("The word code where the d might be replaced by any letter was found %i times" % (count))


def string_input():
    words = raw_input("Please give sentence to search.\n")
    return words

if __name__ == '__main__':
    search_in_string()
