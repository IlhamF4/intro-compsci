def exact_divide_between(n, d):
    """ n and d are positive ints > 1
    
    Returns how many ints from 2 to d divide n evenly. 
    If there are zero, then returns None, but prints 
    "No divisors 2 to d." (replacing d with the actual parameter)
    """
    count = 0
    for i in range(2,d+1):
    	if n % i == 0:
    		count += 1
    if count == 0:
    	print(f"No divisor 2 to {d}")
    	return None
    else:
    	return count
print(exact_divide_between(10,6))   # prints 2
print(exact_divide_between(11,5))   # prints "No divisors 2 to 5" then None
print(exact_divide_between(20,2))   # prints 1