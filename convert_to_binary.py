
def find_highest_power(n):
	"""Find highest power of 2 that is less or equal to n
	
	return is power y where 2**y <= n"""
	upper_bound = 0
	i = 0
	while True:
		if 2**i > n:
			upper_bound = i - 1
			break
		i += 1
	return upper_bound

def convert(n):
	"""convert n from decimal to binary
	
	rerurn value in string form"""
	upper_bound = upper(n)
	binary = ""
	for a in range(upper_bound, -1, -1):
		if 2**a <= n:
			binary += '1'
			n -= 2**a
		else:
			binary += '0'
	return binary

def test_convert(numbers):
	for i in numbers:
		val = ''
		result = convert(i)
		if result == f"{i:b}":
			val = 'correct'
		else:
			val = 'incorrect'
		print(f'{i} conver to binary {result} is {val}')
		
	
vals = (13,8,7)
test_convert(vals)