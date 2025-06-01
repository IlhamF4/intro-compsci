## 6.100A PSet 1: Part A
## Name:
## Time Spent:
## Collaborators:

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################
yearly_salary = int(input('Enter your yearly salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
cost_of_dream_home = int(input('Enter the cost of your dream home: '))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
portion_down_payment = 0.25
amount_saved = 0
r = 0.05
months = 0
dp = cost_of_dream_home * portion_down_payment
monthly_salary = yearly_salary / 12

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################
#calculate how many months to pay for downpayment of dream house

while True:
	months += 1
	investment = amount_saved * (r/12)
	amount_saved = amount_saved + (monthly_salary * portion_saved)
	amount_saved = amount_saved + investment
	if (amount_saved >= dp):
		break

#output
print(f'Number of months: {months}')