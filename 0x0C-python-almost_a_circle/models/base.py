#!/usr/bin/python3
''' module for the Class: Base '''


class Base:
    ''' Base class for all shapes '''
    __nb_objects = 0

    def __init__(self, id=None):
        ''' Initializes a new instance with an id '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
