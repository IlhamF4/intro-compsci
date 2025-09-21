def get_element_lens(L):
    """ L is a list of ints, floats, lists, tuples, or strings.
    
    Returns a list whose elements are the length of each element in L, 
    in the same order they appear in L. If the type of the element is 
    an int or float, the length is the length of its string representation. """
    # your code here
    length = []
    for i in L:
    	if type(i) == int or type(i) == float:
    		length.append(len(str(i)))
    	else:
    		length.append(len(i))
    return length

# Examples
Lin = [5, 8.0, [6,4], (0,), 'ana']
print(get_element_lens(Lin))   # prints [1, 3, 2, 1, 3]