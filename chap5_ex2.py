count = 0			 
total = 0
largest = None
smallest = None

while True:					      num = input('Enter a number: ')
	if num == 'done' : break		      try:
		number = float(num)
	except:
		print('Invalid input')

        if largest is None or number > largest:
		largest = number
	if smallest is None or number < smallest:	
	        smallest = number

	count = count + 1	    
	total = total + number

print(total,count,largest,smallest)
