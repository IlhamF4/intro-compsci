def find_root(x, power, epsilon):
	# Find interval containing answer
	if x < 0 and power % 2 == 0:
		return None # Negative number has no even powered root
	low = min(-1, x)
	high = max(1,x)
	ans = (high + low)/2
	while abs(ans**power - x) >= epsilon:
		if ans**power < x:
			low = ans
		else:
			high = ans
		ans = (high + low)/2
	return ans
	
def test_find_root(x_vals, powers, epsilons):
	for x in x_vals:
		for p in powers:
			for e in epsilons:
				result = find_root(x, p, e)
				if result == None:
					val = 'No root exist'
				else:
					val = 'Okay'
					if abs(result**p - x) > e:
						val = 'Bad'
				print(f'x = {x}, power = {p}, epsilon = {e}: {val}')

x_vals = (0.25, 8, -8)
powers = (1, 2, 3)
epsilons = (0.1, 0.001, 1)
test_find_root(x_vals, powers, epsilons)