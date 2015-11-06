__author__ = 'conor'

# Program to illustrate scoping

def f(x): # Program that add one to is arguemt then prints is out

    x += 1
    y = 1
    print("In function f")
    print "x is %i" % (x)
    print "y is %i" % (y)
    print "z is %i" % (z)

    return x

x, y, z = 5, 10, 15

print "Before function f:"
print "x is %i" % (x)
print "y is %i" % (y)
print "z is %i" % (z)

z = f(x)

print "After function f:"
print "x is %i" % (x)
print "y is %i" % (y)
print "z is %i" % (z)