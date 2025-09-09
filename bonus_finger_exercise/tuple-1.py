def make_ints(t):
    """ t is a tuple
    Returns a tuple whose elements are only the ints within t, 
    in the same order that they appear in t. """
    # your code here
    new_t = ()
    for i in t:
    	if type(i) == int:
    		new_t += (i,)
    return new_t


# Examples
print(make_ints((3,5,'a',7)))  # prints the tuple (3, 5, 7)
