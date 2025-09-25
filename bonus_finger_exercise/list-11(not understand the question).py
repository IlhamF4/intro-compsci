def f(L, val):
    """ L is a non-empty list of ints
        val is a positive int
    If all elements in L are less than val, returns their average. 
    If at least one element in L is greater than val, returns False. """
    # fix this code
    for e in L:
        if e >= val:
            return False
    return sum(L)/len(L)

print(f([1,4,6,7],4))
print(f([1,2,0,3],9))