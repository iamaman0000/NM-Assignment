#Arrays and random numbers
from numpy import random

#Random Number Generation
print("You have to give initial and final value to create an array inbetween those values")
x=int(input("Give initial value:", ))
y=int(input("Give  final value:", ))
n=int(input("Size of array:", ))
def array(x,y,n): 
    s=random.randint(x,y+1,size=(n))
    return s
print("The array of Random Numbers:",array(x,y,n))

#Sorting the array in ascending order
m=array(x,y,n)
for i in range(n):
    for j in range(i+1,n):
        if m[i]>m[j]:
            m[i],m[j]=m[j],m[i]
print("The Ascending order of that array:",m)






