def count_ints(LL):
    """ LL is a list whose elements are lists of ints 
    
    Returns a frequency dict whose keys are unique ints in LL's inner
    lists, and the associated value with a key is a count of how many times 
    that int appears in all inner lists of LL. """
    # your code here
    keylist = []
    seen = []
    for i in LL:
    	for j in i:
    		if j not in keylist:
    			keylist.append(j)
    		seen.append(j)
    
    dict = {}
    for k in keylist:
    	count = 0
    	for s in seen:
    		if k == s:
    			count += 1
    	dict[k] = count
    return dict

LL = [[4],[5],[6],[7]]
print(count_ints(LL))  # prints {4: 1, 5: 1, 6: 1, 7: 1}  
         
LL = [[4,3,2,1],[5,4,5,6,7],[6,2,1],[7,3]]
print(count_ints(LL))  # prints {4: 2, 3: 2, 2: 2, 1: 2, 5: 2, 6: 2, 7: 2}           

LL = [[4,4],[4,4,4,4],[4,4,4],[4]]
print(count_ints(LL))  # prints {4: 10}          