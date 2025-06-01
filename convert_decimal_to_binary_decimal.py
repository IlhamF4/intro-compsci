x = float(3.6)
#input('Enter a decimal number between 0 and 1: '))

# Looking power p that when 2**p * x become a whole number
p = 0
while ((2**p)*x)%1 != 0:
   print(f'Remainder = {str((2**p)*x - int((2**p)*x))}')
   p += 1

num = int(x*(2**p))

# Convert whole number to binary form
result = ''
if num == 0:
    result = '0'
while num > 0:
    result = str(num%2) + result
    num = num//2

for i in range(p - len(result)):
    result = '0' + result

result = result[0:-p] + '.' + result[-p:]
print(f'The binary representation of the decimal {str(x)} is {str(result)}')
