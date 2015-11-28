__author__ = 'conor'

"""
def taking_in_file():
    use reader to take in the file and assin the content to a varaiable
    return file_contents

def search_file():

    file_contents = take_in_file()

    search_item = file_contents("search_item_string")
    search_item = file_contents("search_item_string")
    search_item = file_contents("search_item_string")
    search_item = file_contents("search_item_string")
    search_item = file_contents("search_item_string")

    print ("Results")

    results = create string with results

    return results



"""

import time

def take_in_file():
    file = open('file.txt', 'r')
    #print(file)
    file_contents = file.read()

    return file_contents

def search_file():

    file_contents = take_in_file()

    left_bracket = file_contents.count("<")
    right_bracket = file_contents.count(">")
    new_line = file_contents.count("<br>")
    letter_e = file_contents.count('e')
    string_1 = file_contents.count("<!--")
    string_2 = file_contents.count("-->")

    results = (("< was found %i times, > was found %i times, new line <br> was found %i times, e was found %i times, <!-- was found %i times and --> was found %i times") %
               (left_bracket, right_bracket, new_line, letter_e, string_1, string_2))

    #print results

    return results


def write_out(contents):

    file = open("file_1.txt", 'w')

    file.write(contents)

if __name__ == '__main__':
    write_out(search_file())