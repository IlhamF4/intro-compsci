import copy

def change_to_lens(L):
    """ L is a list of ints, floats, lists, tuples, or strings.
    
    Mutates L to be a list whose elements are the length of 
    that element. If the elements is an int or float, the length 
    is the length of its string representation.  Returns None. """
    # your code here
    Lcopy = copy.deepcopy(L)
    length = []
    for i in range(0,len(Lcopy)):
    	if type(Lcopy[i]) == int or type(Lcopy[i]) == float:
    		L[i] = len(str(Lcopy[i]))
    	else:
    		L[i] = len(Lcopy[i])

# Examples
B = [5, 8.0, [6,4], (0,), 'ana']
print(change_to_lens(B))   # prints None
print(B)        # prints [1, 3, 2, 1, 3]

A = [5, (0,), '6.100L']  
print(change_to_lens(A)) # prints None 
print(A)        # prints [1, 1, 6]