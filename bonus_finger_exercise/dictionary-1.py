def get_keys(d, x):
    """ d is a dict
    Assume a dict entry is a dk,dv pair. Returns a list, in sorted order, 
    of all dict keys, dk, whose associated dv is x. """
    # your code here
    value = []
    for dk, dv in d.items():
    	if dv == x:
    		value.append(dk)
    value.sort()
    return value

# Examples
d = {1:2, 3:4, 5:6}
x = 6
print(get_keys(d, x))  # prints [5]

d = {5:6, 3:4, 1:6}
x = 6
print(get_keys(d, x))  # prints [1, 5]