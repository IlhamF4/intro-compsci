def f(L, val):
    """ L is a list 
        val is an int 
    If all elements in L are less than val, returns their average. 
    If at least one element in L is greater than val, returns False. """
    # fix this code
    for e in L:
        if e >= val:
            return False
    return sum(L)/len(L)

# Examples
# list of all numbers, val a number, and result is True
#print(f([1,2,3,4],5))
# list of all numbers, val a number, and result is False
#print(f([3,5,1,9],6))
# list with nothing in it, val a number
#print(f([],6))
# list that contains numbers and other types, val a number
#print(f([1,2,'5'],5))
# list that contains numbers, val is not a number
#print(f[1,5,7],'t')
