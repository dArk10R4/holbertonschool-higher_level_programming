#!/usr/bin/python3
'''
Module Documentation
'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    class Documentation
    '''
    def __init__(self, size, x=0, y=0, id=None):
        '''
        Method Documentation
        '''
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        '''
        Method Documentation
        '''
        return f"[Square] ({self.id}) \
{self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        '''
        Method Documentation
        '''
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for i, attr in enumerate(attrs):
                if i < len(args):
                    setattr(self, attr, args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''
        Method Documentation
        '''
        dictionary = {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
            }
        return dictionary
