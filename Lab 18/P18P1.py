__author__ = 'conor'

"""

def iterative_test_for_pal():
    take in string

    run loop until middle of word is reached
        comapre outermost letters on either side

        if equal move in one step
            set result = True

        else
            result = False
            break loop

    print result


"""

def iterative_test_for_pal():
    word = string_input()

    if word == 0 or word == 1:
        return True

    start_left_position = 0
    start_right_position = -1

    while start_left_position < ((len(word)/2) +1):
        print("Comparing %s and %s" % (word[start_left_position], word[start_right_position]))
        if word[start_left_position] == word[start_right_position]:
            result = True

            start_left_position += 1
            start_right_position -= 1

        else:
            result = False
            break


    if result == True:
        print("%s is a palidrome" % (word))
    else:
        print("%s is not a palidrome" % (word))

def string_input():
    words = raw_input("Please give a word to check if a palindrome.\n")
    return words.lower()


if __name__ == '__main__':
    iterative_test_for_pal()