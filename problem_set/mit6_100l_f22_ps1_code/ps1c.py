## 6.100A PSet 1: Part C
## Name:
## Time Spent:
## Collaborators:

##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input('Enter the initial deposit: '))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
down_payment = 800_000 * 0.25
epsilon = 100
months = 36
steps = 0
amount_saved, r = 0, 1

low = 0
high = 1.0
ans = (low + high) / 2

##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################
if initial_deposit >= down_payment:
	r = 0.0

while abs(amount_saved - down_payment) > epsilon:
	amount_saved = initial_deposit * (1 + (r/12)) ** months
	if amount_saved < down_payment and steps == 0:
		r = None
		break
	steps += 1
	if amount_saved < down_payment:
		low = ans
	else:
		high = ans
	ans = (high + low) / 2
	r = ans

print(f'Best saving rate: {r} [or very close to this number]')
print(f'Steps in bisection search: {steps} [or very close to this number]')