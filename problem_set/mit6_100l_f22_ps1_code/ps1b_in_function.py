def part_b(yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise):
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
	return months