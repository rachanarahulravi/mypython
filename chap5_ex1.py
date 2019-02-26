count=0
total=0
largest = none
smallest = none
while true:
    num=input('enter a number:')
    if num=='done': 
        break
    try:
        number=float(num)
    except:
        print('invalid input')
    count=count+1
    total=total+number
average=total/count
print(total,count,average)
