#nth Fibonacci Number
def fibo(n):
    a=0
    b=1
    if n==0:
        return a
    elif n==1:
        return b
    else:
        for i in range (2,n+1):
            s=a+b
            a=b
            b=s
        return s



