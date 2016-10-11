#!/usr/bin/python

def power(base, exponent):
    result = base**exponent
    print "%d with exponent %d is %d" % (base, exponent, result)
    return result

power(5,2)

from math import sqrt # import just sqrt from math
# from math import * # import all

print sqrt(27)

def biggest_number(*args):
    print max(args)
    return max(args)

def smallest_number(*args):
    print min(args)
    return min(args)

def distance_from_zero(arg):
    print abs(arg)
    return abs(arg)

biggest_number(5,7,9)
smallest_number(5,7,9)
distance_from_zero(-10)

#check the type of a variable 
print type(34)
print type(3.15)
print type("hola")
