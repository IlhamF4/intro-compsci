'''Using bisection search to find an integer in range 0 <= N <= 1000'''
import random

secret_num = random.randint(0,1000)
count = 0
upper = 1000
lower = 0
ans = (upper + lower) // 2

while ans != secret_num:
	if ans > secret_num:
		upper = ans
	else:
		lower = ans
	ans = (upper + lower) // 2
	count += 1
print('count:', count)
print('answer:', ans)