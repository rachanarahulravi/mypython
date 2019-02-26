
def compare(a,b,c):
    if(a>b) and (a>c):
        largest=a
    elif(b>a) and (b>c):
        largest=b
    else:
        largest=c
    return largest


def compare(a,b,c):
    if a>b:
        if a>c:
            largest=a
        else:
            largest=c
    else:
        if b>c:
            largest=b
        else:
            largesr=c
    return largest
