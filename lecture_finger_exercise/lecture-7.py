def eval_quadratic(a,b,c,x):
	return a*x**2 + b*x + c

def two_quadratic(a1, b1, c1, x1, a2, b2, c2, x2):
	sum = eval_quadratic(a1, b1, c1, x1) + eval_quadratic(a2, b2, c2, x2)
	print(sum)

two_quadratic(1,1,1,1,1,1,1,1)
print(two_quadratic(1,1,1,1,1,1,1,1))