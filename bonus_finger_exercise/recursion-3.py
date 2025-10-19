def score_count(x, d={0:1,1:1,2:2,3:4}):
    """ x is a positive int
        d is a dict
    Returns all the ways to make a score  of x by adding   
    1, 2, and/or 3 together. Order matters. """
    # your code here
    if x in d:
    	return d[x]
    else:
    	ans = score_count(x-1,d) + score_count(x-2,d) + score_count(x-3,d)
    	d[x] = ans
    	return ans

# Examples:
print(score_count(1))  # prints 1
print(score_count(2))  # prints 2
print(score_count(3))  # prints 3
print(score_count(4))  # prints 7
print(score_count(7))  # prints 44
print(score_count(18)) # prints 35890