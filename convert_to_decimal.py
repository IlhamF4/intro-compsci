"""convert binary digit to ots decimal form"""

binary = '1101'
result = 0
# Iterate the string from right to left
for i in range( len(binary)):
	digit = int(binary[-(i + 1)])
	if digit == 0:
		continue
	result += digit * 2**i
print(result)
		