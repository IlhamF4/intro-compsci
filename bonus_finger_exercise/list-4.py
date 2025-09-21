def is_sum(L1, L2, L3):
    """ L1, L2, L3 are lists of equal length, whose elements are numbers
    
    Mutates L1 to have elements that are either True or False. An element at 
    index i is True if L1 at that index is the sum of L2 and L3 at that index.
    It's False otherwise. Returns None.    """
    # your code here
    L1_copy = L1[:]
    for i in range(0,len(L1)):
    	if L1_copy[i] == (L2[i]+L3[i]):
    		L1[i] = True
    	else:
    		L1[i] = False

# Example
L1 = [3,6,1]
L2 = [1,5,7]
L3 = [1,2,-6]
print(is_sum(L1, L2, L3))  # prints None
print(L1)    # prints [False, False, True]