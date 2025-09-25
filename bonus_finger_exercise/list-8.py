def up_to_n(n, as_str = False):
    """ n is an int
        as_str is a bool, default False
    Returns a new list with n elements, in order from 1 to n. 
    If as_str is False, each element is the int version of that int. 
    If as_str is True, each element in is the str version of that int.    
    """
    # your code here
    ele = []
    for i in range(1,n+1):
    	if as_str == True:
    		ele.append(str(i))
    	else:
    		ele.append(i)
    return ele

# Examples
print(up_to_n(4))        # prints the list [1, 2, 3, 4]
print(up_to_n(4, True))  # prints the list ['1', '2', '3', '4']