hours_input = input('Enter Hours: ')
rate_input = input('Enter Rate: ')
hours = float(hours_input) 		
rate = float(rate_input) 	    
if hours < 40:
	pay = rate * hours	    
else:
	times_over = hours // 40 - 1
	overtime = hours % 40	
	pay = 40.0 * rate + times_over * rate * (40 * 1.5) + overtime * rate * 1.5
print('Pay:',pay)
