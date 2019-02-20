
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

def addfractions(f1,f2):
    denominator=f1[1]*f2[1]
    numerator=(f1[0]*f2[1])+(f2[0]*f1[1])
    return[numerator,denominator]

def addfractions(f1,f2):
    d={}
    d[denominator]=f1[1]*f2[1]
    d[numerator]=(f1[0]*f2[1])+(f2[0]*f1[1])
    return d[numerator,denominator]


 from fraction import gcd
class fraction:
    def--init--(self,a,b):
    self.numerator=a
    self.denominator=b
f1=fraction(1,2)
f2=fraction(2,3)
    def --add--(self,other):
        self.sumofn=self.num+otjer.num
        self.sumofd=gcd(self.deno,other.deno)
    return(self.sumofn,self.sumofd)
print(fraction(1,2)+fraction(2,3))

