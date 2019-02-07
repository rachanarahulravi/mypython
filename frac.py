
def add(num1,den1,num2,den):
    den=den1*den2
    num=num1*den2 + num2*den1
    return num,den

def main():
    num,den=add(1,2,1,3)
    print(num,den)
    '''print("%d/%d + %d/%d is %d/%d"%(1,2,1,3,num,den))'''      
    
def addfractions(f1,f2):
    denominator=f1[1]*f2[1]
    numerator=(f1[0]*f2[1])+(f2[0]*f1[1])
    return(numerator,denomimator)
