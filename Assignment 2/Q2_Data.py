#importing all the external modulues
import numpy as np
import matplotlib.pyplot as plt

#importing the data given to us
x,y=np.loadtxt("data.dat",unpack=True)

'''Part 'a' '''
#Lagrange's interpolation
def lagrange_interpolation(a):   #Here 'a' is the value where we want interpolated data
    p=0     #giving the initial value
    for i in range(len(x)):  #This code is implication of Lagrange's multiplier
        L=1
        for j in range(len(x)):    #This loop is for finding polynomial for every index
            if i!=j:
                L=((a-x[j])/(x[i]-x[j]))*L  
        m=(y[i]*L)                #Multiplying of polynoimal of a index to it's y's value
        p=p+m                     #summing up all polynoimal to get interpolated value
    return p
print("The Interpolated data in x=2.5 is",lagrange_interpolation(2.5))   #Printing value of Interpolated data at given point

'''part 'b' '''
#Lagrange differentiation of any point
def lagrange_diff(a):        #Here 'a' is the value where we want the value of differentiation
    p=0
    for i in range (len(x)):
        L=1
        k=0
        for j in range (len(x)):     
            if i!=j:
                L=((a-x[j])/(x[i]-x[j]))*L
                k=k+(1/(a-x[j]))
        l=L*k                     #Finding polynoimal for every index
        m=(y[i]*l)                #Multiplying of polynoimal of a index to it's y's value
        p=p+m                     #summing up all polynoimal to get differentiated value for any point
    return p
#Finding roots by newton-raphson method
def root(a,f,g):                    #Here 'a' is initial value and 'n' is error tolerance we want
    while abs(f(a))>0.0001:    #this is the code for newton-raphson
        a=a-(f(a)/g(a))
    return a
#Basically we know there are two real roots so we choose our initial value accordingly so we will get the two roots
#Printing two roots
print("The two roots of given data is:",root(3,lagrange_interpolation,lagrange_diff),root(-1,lagrange_interpolation,lagrange_diff))

'''Part 'c' '''
#Defining code for Integration by simpson Method
def simpson(a,b,f):
    n=10   #Here 'a' is Initial value,'b' is Final Value, 'f' is function 
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
#Printing the value of Integration of the given data from 0 to 4
print("The Integration value of the data from 0 to 4 is:",simpson(0,4,lagrange_interpolation))

'''Part 'd' '''
#There are no points where the value of the integration from 0 to that point would be zero
#So, Tutor told me to find the point where the value of the integration from 0 to that point would be 5
def simp(a):   #I have changed the dimension of arguments
    return simpson(0,a,lagrange_interpolation)

def int_five(a,f,g):  #Code for to find the point
    while abs(f(a))>5.00001:
        a=a-((f(a)-5)/g(a))
    return a

print("The value where integration from 0 will be 5 is:",int_five(4.5,simp,lagrange_interpolation))

'''part e'''
#Code for 2nd differentiation of the given data
def diff_2nd(a):
    h=0.001
    return ((-lagrange_diff(a+2*h) + 8*lagrange_diff(a+h) - 8*lagrange_diff(a-h) + lagrange_diff(a-2*h))/(12*h))
#Code for 3rd differetiation of the given data
def diff_3rd(a):
    h=0.001
    return ((-lagrange_diff(a+2*h) + 16*lagrange_diff(a+h) - 30*lagrange_diff(a) + 16*lagrange_diff(a-h) - lagrange_diff(a-2*h))/(12*(h**2)))
#This is the function of 'w', by solving it's roots we will get value of w
def f(w):
    return (lagrange_interpolation(0)*(w**3) - 3*lagrange_diff(0)*(w**2) + 3*diff_2nd(0)*w - diff_3rd(0))
#This is the differentiation of the function of w
def g(w):
    return (3*lagrange_interpolation(0)*(w**2) - 6*lagrange_diff(0)*w + 3*diff_2nd(0))

w=root(2,f,g)            #Finding w, w is the root of the function f()
c=lagrange_interpolation(0)   #Finding c
b=lagrange_diff(0)-(c*w)      #Finding b
a=(diff_2nd(0)-(2*b*w)-c*(w**2))/2   #Finding a
print("The value of a is:",a)
print("The value of b is:",b)
print("The value of c is:",c)
print("The vale of w is:",w)
#The function we have assumed
def function(x):
    return ((a*(x**2)+(b*x)+c)*np.exp(w*x))


                                                                                                           

        
#Plot through it was not given in the question
plt.plot(x,function(x),'red',label="(ax^2+bx+c)exp(wx)")
plt.grid()
plt.scatter(x,y,label="Given Data")
plt.show()
plt.xlabel("X")
plt.ylabel("Y")
