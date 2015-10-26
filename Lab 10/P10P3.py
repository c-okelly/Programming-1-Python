__Author__ = "Conor O'Kelly"

"""
pysudocode

word = function of request raw input from user

check if word blank

if ! blank:
    split word into list
    for in in list
        count voewls
    return result of count

Print results of count or exit if blank

"""

def main():

    word = get_string()

    while word != "":
        count = count_vowels(word)

        print "There is %s vowel(s) in %s" % (count, word)
        word = get_string()
        
    print "You have entered a blank string. Program is now ended"
    
    

def count_vowels(string):

    vowels_count = 0
    string_list = list(string)

##    print string_list

    for i in string_list:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "" or i == "u":
            vowels_count += 1
            
    return vowels_count

def get_string():

    string = raw_input ("Please enter a string \n")
    string = string.lower()

    return string

#Test 1

main()
