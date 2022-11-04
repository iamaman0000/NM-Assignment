#Prime Numbers
n=int(input("Enter the Number:",))
l=[]
for i in range(2,n+1):
    for j in range(2,i):
        if i%j==0:
           break
    else:
       l.append(i)
print("List of Prime Numbers till",n,"is",l)

