def add_ops(func, num, s):
    """ func is a function that takes in an int or str and returns an int
        num is an int
        s is a str
    Prints 'check input' if num is not an int or s is not a str. 
    Otherwise, it returns the sum of the result when you run 
    func on num with the result when you run func on s.   
    """
    if type(num) != int or type(s) != str:
    	print('check input')
    else:
    	return func(num) + func(s)

## Examples of func:
def num_chars(a):
    if type(a) == str:
        return len(a)
    if type(a) == int:
        return len(str(a))

def always_0(a):
    return 0

# Examples
print(add_ops(num_chars, 74, 'abc'))  # prints 5
print(add_ops(always_0, 74, 'abc'))   # prints 0