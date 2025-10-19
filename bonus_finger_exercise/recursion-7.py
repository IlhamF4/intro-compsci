def is_str_in(L, s):
    """ L is a list whose elements are either strs or lists, 
            and whose inner-lists are either strs or lists, etc.
        s is a string
    Returns True if s is in L or any of the inner-lists of L """
    # your code here
    if L == []:
    	return False
    elif type(L[0]) == str:
    	return L[0] == s or is_str_in(L[1:],s)
    else:
    	return is_str_in(L[0],s) or is_str_in(L[1:],s)

# Examples
#L = ['a','b',['c','defg',['h',['ijk']]]]
#print(is_str_in(L, 'd'))        # prints False
#L = ['a','b',['c','defg',['h',['ijk']]]]
#print(is_str_in(L, 'defgh'))    # prints False
L = ['a','b',['c','defg',['h',['ijk']]]]
print(is_str_in(L, 'h'))        # prints True
L = ['a','b',['c','defg',['h',['ijk']]]]
print(is_str_in(L, 'a'))        # prints True