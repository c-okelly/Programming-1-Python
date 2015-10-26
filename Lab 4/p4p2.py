# Author Conor O'Kelly
# Date 29/9/15
# Student number = 15203728

from math import pi

number = 1520.3738

def shape_calculator(length):
    if length <= 0:
        print "The length must be greater then zero. Please try again."
    else:
        square = length * 2
        print "The area of the square is", square
        cube_volume = length ** 3
        print "The volume of the cube is", cube_volume 
        area_circule = ((length**2) * pi)
        print "The area of the circle is", area_circule
        volume_sphere = ((4/3) * pi * (length**3))
        print "The volume of the sphere", volume_sphere
        volume_cylinder = (length * (length**2) * pi)
        print "The volume of the cylinder is", volume_cylinder


#Test 1
print "Test 1 - Less then zero amount"
shape_calculator(0)

#Test 2
print "\nTest 2 - student number amount."
shape_calculator(number)
