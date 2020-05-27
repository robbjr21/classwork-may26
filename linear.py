#linear.py
def linearfunction(a,b,x):
    slope = (a[1] - b[1])/(a[0] - b[0])
    yint = a[1] - slope*a[0]
    return x*slope+yint

print(linearfunction((0,0),(2,2), 10))
