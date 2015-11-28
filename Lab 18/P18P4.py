__author__ = 'conor'

"""
def search_in_string():
    words_list = used to generate the list of items for program

    assign different elements

    create pattern 1
    create pattern 2

    search for pattern 1
    search for pattern 2

    print result of pattern found

"""

def search_in_string():
    words_list = string_input()

    sentance_list = words_list[0]
    code_1 = words_list[1]
    code_2 = words_list[2]

    pattern_1 = code_1 + code_2
    pattern_2 = code_2 + code_1


    f1 = sentance_list.count(pattern_1)

    f2 = sentance_list.count(pattern_2)

    print ("The combination of %s was found %i times. The combination of %s was found %i times" % (pattern_1,f1,pattern_2,f2))

    #print(f1,f2)

def string_input():
    list_items = []

    words = raw_input("Please give sentence to search.\n")
    string_1 = raw_input("Please give code word 1 to search for.\n")
    string_2 = raw_input("Please give code word 2 to search for.\n")

    list_items.extend((words.lower(),string_1.lower(),string_2.lower()))
    return list_items

if __name__ == '__main__':
    search_in_string()
