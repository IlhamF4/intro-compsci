class UniqueItems(object):
    """ A group of items that contains NO DUPLICATES """
    def __init__(self, items):
        items_list = []
        """ items is a list """
        # your code here
        for i in items:
        	if i not in items_list:
        		items_list.append(i)
        self._items = items_list[:]
        items_list.clear()

    def add_item(self, item):
        """ Adds items to self """
        # your code here
        if item not in self.get_items():
        	self.get_items().append(item)

    def remove_item(self, item):
        """ Removes item from self """
        # your code here
        self.get_items().remove(item)
        
    def get_items(self):
        """ Returns a list of items in self, in sorted order """
        # your code here
        self._items.sort()
        return self._items

    def __str__(self):
        """ Returns a str representing the sorted group of items in self,
            separated by commas and then a space """    
        # your code here
        return ', '.join(str(v) for v in self.get_items())
            

def make_uniques(LL):
    """ LL is a list, whose elements are lists of ints
    Returns a UniqueItems object whose items are the union 
    of all elements in all lists of LL. """
    # your code here
    p = UniqueItems([])
    for i in LL:
       for j in i:
       	p.add_item(j)
    return p
       
# Examples     
L = [[3,2,1], [5,8], [2], [7,9]]    
u = make_uniques(L)
print(u.get_items())  # prints [1, 2, 3, 5, 7, 8, 9]

L = [[3,3,3], [3,3], [1]]    
u = make_uniques(L)
print(u.get_items())  # prints [1, 3]