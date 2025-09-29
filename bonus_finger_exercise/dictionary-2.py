def remove_with_val(d, x):
    """ d is a dict
    Assume a dict entry is a dk,dv pair. Mutates d so that all dict entries 
    whose dict value, dv, is x are removed from d. Returns None. """
    # fix this code
    dNew = d.copy()
    d.clear()
    for k,v in dNew.items():
        if v != x:
            d[k] = v
            


# Examples
d = {1:2, 3:4, 5:6}
x = 6
remove_with_val(d, x) 
print(d)   # prints {1: 2, 3: 4}

d = {5:6, 3:4, 1:6}
x = 6
remove_with_val(d, x) 
print(d)   # prints {3: 4}