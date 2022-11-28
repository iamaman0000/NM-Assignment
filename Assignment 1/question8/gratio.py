#Golden Ratio
import numpy as np
import matplotlib.pyplot as plt

#Import the function
import sys
sys.path.insert(0,'/home/aman/assignment1/question5')
import fibo as fb

#The ratio of two consecutive Fibonacci Numbers
n=int(input("Enter the Number:",))
def ratio(n):
    return(fb.fibo(n+1)/fb.fibo(n))
print("Ratio of",n+1,"th and",n,"th fibonacci number is:",ratio(n))

#Plot of Golden Ratio
L=[]
m=np.linspace(1,100,100)
for i in range(1,101):
    L.append(fb.fibo(i+1)/fb.fibo(i))
plt.plot(m,L,'-o')
plt.xlabel("Natural Numbers")
plt.ylabel("The Ratio of two consecutive fibonacci numbers")
plt.title("Golden Ratio")
plt.grid()
plt.show()

