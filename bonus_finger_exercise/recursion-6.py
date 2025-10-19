def sum_lengths(L):
    """ L is a list whose elements are either strs or lists, 
        and whose inner-lists are either strs or lists, etc.
    Returns the length of all strings in L and all inner-lists of L. """
    # your code here
    if L == []:
    	return 0
    elif type(L[0]) == str:
    	return len(L[0])+sum_lengths(L[1:])
    else:
    	return sum_lengths(L[0]) + sum_lengths(L[1:])

# Example
L = ['a','b',['c','defg',['h',['ijk']]]]
print(sum_lengths(L))    # prints 11