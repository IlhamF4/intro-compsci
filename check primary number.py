#Program to check sum of primary number from 3 to 1000

sum = 0
divisible = 0

for i in range(3,1000):
	divisible = 0
	#check if number is primary number
	for j in range(1,1000):
		if i % j== 0:
			divisible += 1
		if divisible > 2:
			break
	if divisible == 2:
		sum += i
print(sum)