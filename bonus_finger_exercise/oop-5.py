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
        
# Examples
grocery = Todo('To Buy')
grocery.add_todo('oranges')
grocery.add_todo('coffee')
grocery.add_todo('milk')
grocery.add_todo('pizza')
grocery.add_todo('coffee')
grocery.add_todo('coffee')
print(grocery)
print()
grocery.mark_off('coffee')
print(grocery)
print()
print(grocery.get_item_list())  # prints ['milk', 'oranges', 'pizza']
print(grocery.get_name())       # prints To Buy

stuff = Todo('Tasks')
stuff.add_todo('make friends')
stuff.add_todo('be optimistic')
stuff.add_todo('study for exams')
stuff.add_todo('sleep 8 hours')

stuffnthings = stuff+grocery
print(stuffnthings.get_name())      # prints Tasks AND To Buy
print(stuffnthings.get_item_list()) # prints ['be optimistic', 'make friends', 'milk', 'oranges', 'pizza', 'sleep 8 hours', 'study for exams']