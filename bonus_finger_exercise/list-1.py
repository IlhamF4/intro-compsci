def count_ints(L):
    """ L is a list
    Returns how many elements in L are ints. """
    # your code here
    count = 0
    for i in L:
    	if type(i) == int:
    		count +=1
    return count
    
# Examples
print(count_ints([3,5,'a',7]))  # prints 3
