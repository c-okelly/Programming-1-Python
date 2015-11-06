__author__ = 'conor'

# Another program to illustrate scoping

def setter(a,b,c): # Does some varialbe  setting for local and global

    print "In setter function"

    a += 5
    b += 1
    c -= 3

    print "Before during setter:"
    print "a is %i" % (a)
    print "b is %i" % (b)
    print "c is %i" % (c)

    return a, b

a,b,c = 1, 4, 10

print "Before function setter:"
print "a is %i" % (a)
print "b is %i" % (b)
print "c is %i" % (c)

setter(a,b,c)

print "Before afters setter:"
print "a is %i" % (a)
print "b is %i" % (b)
print "c is %i" % (c)