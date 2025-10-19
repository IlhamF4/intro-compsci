def count_in(L, e):
    """ L is a list whose elements are either ints or lists, 
        and whose inner-lists are either ints or lists, etc.
        e is an int
    Returns how many times e occurs in L, and any inner-lists of L, etc.
    """
    # your code here
    if L == []:
    	return 0
    elif type(L[0]) == int:
    	if L[0] == e:
    		return 1+count_in(L[1:],e)
    	else:
    		return 0 + count_in(L[1:],e)
    else:
    	return count_in(L[0],e) + count_in(L[1:],e)

# Examples:
L = [4,7,9,1,9,3,9,4]
print(count_in(L, 9))   # prints 3
L = [4,7,9,1,9,3,9,4]
print(count_in(L, 0))   # prints 0
L = [4,[7,[9,1]],[1,[9,9,[9,8,[9]],3],9,4]]
print(count_in(L, 9))   # prints 6
L = [4,[7,[9,1]],[1,[9,9,[9,8,[9]],3],9,4]]
print(count_in(L, 0))   # prints 0