__author__ = 'conor'


"""

recursive functions used in class today


"""

def is_pal(word):

    if len(word) == 0 or len(word) == 1:
        print("Character %s matches itself" % (word))
        return True
    else:
        print("Currently testing letter %s and letter %s" % (word[0], word[-1]))
        print "Result is", (word[0] == word[-1])
        result = (is_pal(word[1:-1]) and  word[0] == word[-1])
        return result

def test_for_palidrome():

    word =string_input()
    result = is_pal(word)

    if result == True:
        print("The word %s is a palidrome" % (word))
    else:
        print("The word %s is not a palidrome" % (word))


def string_input():
    words = raw_input("Please give a word to check if a palidrome.\n")
    return words.lower()

if __name__ == '__main__':
    test_for_palidrome()
