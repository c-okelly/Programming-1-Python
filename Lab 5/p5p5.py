#__Author__ = "Conor O'Kelly"

def town_checker(name):
    cities = ["dublin", "belfast", "cork", "limerick", "derry",
"galway", "lisburn", "kilkenny", "waterford", "sligo"]
    
    name_lower = name.lower()

    if name_lower in cities:
        print "You enterd the name %s and it was found! \n" % (name)
    else:
        print "Sorry, I didn't recognise that name \n"


# Test 1
print " Test 1 - Town name is in list =>  Dublin"
town_checker("Dublin")

# Test 2
print " Test 2 - Town name is not in list => Dubai"
town_checker("Dubai")
