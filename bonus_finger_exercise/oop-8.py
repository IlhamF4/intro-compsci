class Quadrilateral(object):
    """ A class to represent a quadrilateral by 4 points. """

    def __init__(self, topleft, topright, botright, botleft):
        """ topleft, topright, botleft, botright are tuples with 2 elements, 
            representing the 4 corners of a quadrilateral """
        # hidden implementation
        self.topleft = topleft
        self.topright = topright
        self.botright = botright
        self.botleft = botleft
        
    def get_coordinates(self):
        """ Returns a tuple with 4 elements, in this order: 
            * the top-left x,y coord
            * the top-right x,y coord
            * the bot-right x,y coord
            * the bot-left x,y coord """
        # hidden implementation
        return (self.topleft, self.topright, self.botright,self.botleft)
        
    def get_topleft_topright_length(self):
        """ Returns the length between the top-left and top-right coordinates """   
        # hidden implementation
        return abs(self.topleft[0] - self.topright[0])
        
    def get_topright_botright_length(self):
        """ Returns the length between the top-right and bottom-right coordinates """        
        # hidden implementation
        return abs(self.topright[1] - self.botright[1])
        
    def get_botright_botleft_length(self):
        """ Returns the length between the bottom-right and bottom-left coordinates """        
        # hidden implementation
        return abs(self.botright[0] - self.botleft[0])
        
    def get_botleft_topleft_length(self):
        """ Returns the length between the bottom-left and top-left coordinates """        
        # hidden implementation
        return abs(self.botleft[1] - self.topleft[1])
        
    def compute_area(self):
        """ Returns the area of self """
        # hidden implementation
        return self.get_botleft_topleft_length() * self.get_topleft_topright_length()
        
    def compute_perimeter(self):
        """ Return the perimeter of self """
        # hidden implementation
        a = self.get_topleft_topright_length() + self.get_topright_botright_length()
        b = self.get_botright_botleft_length() + self.get_botleft_topleft_length()
        return  a+b


class Rectangle(Quadrilateral):
    """ A class to represent a rectangle centered on the origin. """

    def __init__(self, width, height):
        """ width and height are positive, even ints """
        # your code here
        self.width = width
        self.height = height
        
    def compute_area(self):
    	return self.width * self.height
    
    def compute_perimeter(self):
    	return 2*(self.width + self.height)
    
    def get_width_and_height(self):
        """ Retruns a tuple with the first element representing
        the width and the second elements representing the height """
        # your code here
        return (float(self.width),float(self.height))

# Examples
my_rectangle = Rectangle(10, 5)
print(my_rectangle.compute_area())      # prints 50
print(my_rectangle.compute_perimeter()) # prints 30
print(my_rectangle.get_width_and_height())  # prints (10.0, 5.0)