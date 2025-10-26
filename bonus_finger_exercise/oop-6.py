class Todo(object):
    """ A Todo object has a name and a SORTED list of things to do """
    def __init__(self, name, items_list=None):
        """ name is a string
            items_list is a list, by default empty
        Initializes as Todo object """
        # your code here
        self._name = name
        self._items_list = [] if items_list is None else items_list
        self.sorted = False
            
    def add_todo(self, item):
        """ Adds an item to self """
        # your code here
        self.get_item_list().append(item)
    
    def mark_off(self, item):
        """ Removes all instances of item from self """
        # your code here
        newlist = self.get_item_list()[:]
        self.get_item_list().clear()
        for s in newlist:
        	if s != item:
        		self.get_item_list().append(s)

    def get_name(self):
        """ Returns the name of self """
        # your code here
        return self._name
    
    def get_item_list(self):
        """ Returns a copy of self's sorted items """
        # your code here
        return self._items_list
    
    def __add__(self, other):
        """ other is a Todo object
        Combines Todo objects and returns a new Todo object (may have duplicates) whose:
        * name is self's name concatenated with 'AND' concatenated with other's name. 
                e.g. if self's name is My Stuff and other's name is Your Stuff, 
                the combined name is My Stuff AND Your Stuff
        * items are sorted in alphabetical order """
        # your code here
        name = f"{self.get_name()} AND {other.get_name()}"
        union_list = self.get_item_list() + other.get_item_list()
        union_list.sort()
        return Todo(name,union_list)
        
    def __str__(self):
        """ Returns all items in self, one on each line, sorted in alphabetical order. """
        # your code here
        if self.sorted == False:
        	self.get_item_list().sort()
        text = ""
        for s in self.get_item_list():
        	text = text + s + "\n"
        return text

def checkoff(s1, s2):
    """ s1 and s2 are strings of letters and spaces separated by commas
           for ex: "To Visit,Spain,Brazil,Canada,Spain,Japan,India"
    Returns a Todo object whose 
    * name is the part of s1 until the first comma
    * things in the object are the parts in s1 between subsequent commas
      or the end of s1, without the things in s2 between subsequent commas
      or the end of s2
    """
    # your code here
    newlist = s1.split(',')
    p = Todo(newlist[0],newlist[1:])
    for s in p.get_item_list():
    	p.mark_off(s)
    return p

# Examples
s1 = "To Visit,Spain,Brazil,Canada,Spain,Japan,India"
s2 = "Brazil,Spain,India,Japan"
visit = checkoff(s1, s2)
print(visit.get_item_list())