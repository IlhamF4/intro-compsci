## 6.100A PSet 1: Part B
## Name:
## Time Spent:
## Collaborators:

##########################################################################################
## Get user input for yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise below ##
##########################################################################################
yearly_salary = int(input('Enter your yearly salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
cost_of_dream_home = int(input('Enter the cost of your dream home: '))
semi_annual_raise = float(input('Enter the semi-annual raise, as decimal: '))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
amount_saved = 0
r = 0.05
months = 0
portion_down_payment = 0.25
dp = cost_of_dream_home * portion_down_payment

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################
while True:
	months += 1
	investment = amount_saved * (r/12)
	amount_saved = amount_saved + (yearly_salary  / 12 * portion_saved)
	amount_saved = amount_saved + investment
	if (amount_saved >= dp):
		break
	if (months % 6 == 0):
		yearly_salary += (yearly_salary * semi_annual_raise)

#output
print(f'Number of months: {months}')
