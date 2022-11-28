#importing all the external modulues
import numpy as np

#Defined the given function
def f(x):
    return (x*np.log(x))-x

#This is the code for Trapezoidal ALgorithm
def Trapezoidal(a,b,f):    #a=inital value, b= Final Value, f=Function
    n=1000   
    h=(b-a)/n
    g=(f(a)+f(b))/2
    for i in range (1,n):
        g=g+f(a+i*h)
    area=h*g
    return area

#This is the code for simpson algorithm
def Simpson(a,b,f):
    n=1000  #Here 'a' is Initial value,'b' is Final Value, 'f' is function 
    h=(b-a)/n
    g=f(a)+f(b)
    for i in range (1,n,2):
        x_i=a+(i*h)
        g=g+4*f(x_i)
    for j in range (2,n,2):
        x_j=a+(j*h)
        g=g+2*f(x_j)
    A=(h/3)*g
    return A

print("The value of Integration using Trapezoidal method is:",Trapezoidal(1,3,f))
print("The value of Integration using Simpson method is:",Simpson(1,3,f))


