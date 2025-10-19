def make_d(L):
    """ L is a list with an even number of numerical elements 

    Returns a dictionary whose keys are the numbers at odd positions in L
    and the value associated with each key is the number at the even position
    immediately following an odd one. If there are many numbers at odd positions
    that are the same, pick the first one that appears in L to keep in the dict."""
    # your code here
    keylist = []
    dict = {}
    for i in range(len(L)):
    	if i % 2 == 0 and L[i] not in keylist:
    		dict[L[i]] = L[i+1]
    		keylist.append(L[i])
    return dict

L = [4,5,6,7]
print(make_d(L))  # prints {4:5, 6:7}            

L = [4,1,5,1,6,1]
print(make_d(L))  # prints {4:1, 5:1, 6:1}            

L = [4,1,4,5,6,1]
print(make_d(L))  # prints {4:1, 6:1}          