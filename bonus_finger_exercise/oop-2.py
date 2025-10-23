class Rectangle(object):
    """ A class to represent a rectangle. """

    def __init__(self, width, height):
        """ width and height are ints """
        # your code here
        self.width = width
        self.height = height

    def compute_area(self):
        """ Returns the area of self """
        # your code here
        return self.width * self.height
    
    def compute_perimeter(self):
        """ Return the perimeter of self """
        # your code here
        return 2*(self.height + self.width)
    
    def is_square(self):
        """ Returns True if the width equals the height, and False otherwise """
        # your code here
        return self.width == self.height

# Examples:
my_rectangle = Rectangle(10,5)
print(my_rectangle.compute_area())      # prints 50
print(my_rectangle.compute_perimeter()) # prints 30
print(my_rectangle.is_square())         # prints False