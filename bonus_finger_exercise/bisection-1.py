# Using bisection within alphabet order
secret_letter = 'h'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
letter_low = 'a'
letter_high = 'z'

# change variable to index position
secret = alphabet.index(secret_letter)
low = alphabet.index(letter_low)
high = alphabet.index(letter_high)
ans = (high + low) // 2
guess = 0

#use bisection search
while ans != secret:
	if ans < secret:
		low = ans
	else:
		high = ans
	ans = (high + low) // 2
	guess += 1
print(f'found {alphabet[ans]} after {guess} guesses')