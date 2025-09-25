def get_duplicates(L, verbose=False):
    """ L is a list of ints
        verbose is a boolean, used for debugging prints
    Returns a sorted list containing the all elements in 
    L (without repeating) that occur more than once in L """
    # fix this code
    unique = []
    duplicate = []
    for e in L:
        if e not in unique:
        	unique.append(e)
        elif e not in duplicate:
        	duplicate.append(e)
    return duplicate

# Examples
L = [1,2,3,2,3]
print(get_duplicates(L))  # prints [2,3]

L = [4,2,3,2,3,1,5,4,4]
print(get_duplicates(L))  # prints [2,3,4]