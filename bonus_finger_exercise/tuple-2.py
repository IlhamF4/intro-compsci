def median(*nums):
    """ nums is a non-empty tuple of numbers in increasing order
    
    If nums has an odd number of elements, returns the value of the 
    middle one. Otherwise, returns the average of the middle two numbers.  """
    # your code here
    mid = len(nums) // 2
    if len(nums) % 2 != 0:
    	return nums[mid]
    else:
    	return (nums[mid] + nums[mid-1])/2


# Examples
print(median(3,5,8,9,10))  # prints 8
print(median(3,5,8,9))     # prints 6.5