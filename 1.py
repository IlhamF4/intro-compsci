def log(x, base, epsilon):
	"""Assume x and epsilon int or float, base an int, x > 1, epsilon > 0 & power >= 1
	Return float y such that base**y is within epsilon of x"""
	lower_bound = 0
	# Find lower_bound value
	while base**lower_bound < x:
		lower_bound += 1
	low = lower_bound - 1
	high = lower_bound + 1
	ans = (high + low)/2
	
	#  Perform bisection search
	while abs(base**ans - x) >= epsilon:
		if base**ans < x:
			low = ans
		else:
			high = ans
		ans = (high + low)/2
	return ans

def test_log(x_vals, bases, epsilons):
	for x in x_vals:
		for b in bases:
			for e in epsilons:
				result = log(x, b, e)
				if result != None:
					val = "Okey"
				else:
					val = "Not okey"
				print(f'x = {x}, base = {b}, epsilon = {e}, result = {val} it is {result}')
				
x_vals = (2, 9, 104)
bases = (80, 3, 8)
epsilons = (0.1, 0.001, 1)
test_log(x_vals, bases, epsilons)
	