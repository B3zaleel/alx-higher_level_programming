#!/usr/bin/python3
'''A module containing a class with restrictions.
'''


class LockedClass:
    '''Represents a class with restricted attribute modification.
    '''
    def __setattr__(self, name, value):
        '''Sets an attribute of this class.
        '''
        if name == "first_name":
            self.__dict__[name] = value
        else:
            msg = "'LockedClass' object has no attribute '{}'".format(name)
            raise AttributeError(msg)
