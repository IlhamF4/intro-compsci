class UniqueItems(object):
    """ A group of items that contains NO DUPLICATES """
    def __init__(self, items):
        items_list = []
        """ items is a list """
        # your code here
        for i in items:
        	if i not in items_list:
        		items_list.append(i)
        self.items = items_list[:]
        items_list.clear()

    def add_item(self, item):
        """ Adds items to self """
        # your code here
        if item not in self.items:
        	self.items.append(item)

    def remove_item(self, item):
        """ Removes item from self """
        # your code here
        self.items.remove(item)
        
    def get_items(self):
        """ Returns a list of items in self, in sorted order """
        # your code here
        self.items.sort()
        return self.items

    def __str__(self):
        """ Returns a str representing the sorted group of items in self,
            separated by commas and then a space """    
        # your code here
        return ', '.join(str(v) for v in self.items)
            
# Examples
u1 = UniqueItems([4,6,2,4,6,4])
print(u1.get_items())   # prints [2, 4, 6]
u1.add_item(6)
print(u1.get_items())   # prints [2, 4, 6]
u1.add_item(0)
print(u1.get_items())   # prints [0, 2, 4, 6]
u1.remove_item(2)
print(u1.get_items())   # prints [0, 4, 6]
print(u1)               # prints 0, 4, 6