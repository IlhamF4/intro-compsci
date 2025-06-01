binary = "1001.011"
p = 0
coma = 0
#find coma and power
for i in binary:
	if i == '.':
		coma = binary.index(i)
		p = (len(binary) - 1) - coma

# Form binary without coma
binary = binary[0:coma] + binary[coma + 1:]
binary = binary[::-1]

result = 0
for i in range(len(binary)):
	result = result + int(binary[i]) * 2**i
print(result / 2**p)