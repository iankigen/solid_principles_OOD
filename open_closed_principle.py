"""
A class should be easily extendable without modifying the class itself

In Python we are able to change the functionality of any method, class or function at will. We can even add methods to
classes (or individual instances!) at run-time. For example, imagine we had created a GeometricRectangle using our
previous example, but in order to make it fit into a badly designed API which insisted on the object having a name()
attribute we might consider the following solution:
"""


class GeometricRectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


shape = GeometricRectangle(2, 5)


def name():
    return "I'm a rectangle"


shape.name = name()
print(shape.name)  # Prints: I’m a rectangle
