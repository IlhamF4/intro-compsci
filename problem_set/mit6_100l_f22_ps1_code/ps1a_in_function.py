def part_a(yearly_salary, portion_saved, cost_of_dream_home):
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
	return months