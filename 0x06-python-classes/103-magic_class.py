#!/usr/bin/python3
import math


class MagicClass:
    '''Represents an object for working with circles.'''
    def __init__(self, radius):
        '''Initializes this magic class
        '''
        self.__radius = 0
        if (type(radius) is not int) or (type(radius) is not float):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        '''Computes the area of this circle.'''
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        '''Computes the circumference of this circle.'''
        return 2 * math.pi * self.__radius
