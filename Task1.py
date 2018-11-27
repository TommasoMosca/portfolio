#This script calculates the volume of a sphere of diameter 10 and print it to the screen
from math import pi

# diameter= input('type the diameter of the sphere for which you want to calculate the volume: ')

in_file= open('input_diameter.txt')

diameter=input("type the diameter of the sphere for which you want to calculate the volume: ")
radius=float(diameter)/2.0
volume=(4.0/3)*(pi)*(radius**3)
print ("volume of the sphere: %f" %(volume))
