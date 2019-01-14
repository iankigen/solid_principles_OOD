"""
A Class should be responsible for a single task or a class must have a specific purpose. The idea behind this principle
is that each of your classes, modules, methods are responsible for one and only one thing.
"""


# Given a class which has two responsibilities

class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def draw(self):
        # Do some drawing
        pass

    def area(self):
        return self.width * self.height


# We can split it into two classes with single responsibilities which helps if we ever have an issue with e.g draw
class GeometricRectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class DrawRectangle:
    def draw(self):
        # Do some drawing
        pass
