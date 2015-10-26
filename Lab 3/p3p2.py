
from math import pi

def shape_calculator(length):
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


shape_calculator(4)
