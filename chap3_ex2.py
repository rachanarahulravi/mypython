hours_input = input('Enter Hours: ')
try:
	hours = float(hours_input) 	
except:
	print('Error,  enter numeric input')
	quit()
rate_input = input('Enter Rate: ') 	
try:
	rate = float(rate_input)
except:
	print('Error,  enter numeric input')
	quit()
if hours < 40:
	pay = rate * hours		    
else:
	times_over = hours // 40 - 1	    
	overtime = hours % 40
	pay = 40.0 * rate + times_over * rate * (40 * 1.5) + overtime * rate * 1.5
print('Pay:',pay)
