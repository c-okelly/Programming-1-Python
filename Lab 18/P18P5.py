__author__ = 'conor'

"""
def search_in_string():
    use string input to get sentence and code word

    using index to find an example of the code in the sentence
        return the position number of the segment found

    if segment is found
        check the character before it is not .
            if so print result
    else
        print that phrase was not found

"""


def search_in_string():

    sentence, code = string_input()

    position = sentence.index(code)

    if position != 0:
        if sentence[position-1] != '.':
            print ("The phrase %s was found and was not proceeded by a . " % (code) )
        else:
            print ("The phrase %s was found but was proceeded by a . " % (code) )
    else:
        print ("The phrase %s not found" % (code) )
    print(position)
    print(sentence[5])

    #print("The word code where the d might be replaced by any letter was found %i times" % (count))


def string_input():
    words = raw_input("Please give sentence to search.\n")
    code = raw_input("Please give a string to search for\n")
    return words, code

if __name__ == '__main__':
    search_in_string()
