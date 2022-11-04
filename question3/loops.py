#Loops-Finding sum of the cubes with a function
n=int(input("Enter the number till you want to take sum of cubes:" ))
def cubes(m,n):
    s=0
    for i in range(m,n+1):
        s=s+i**3
    return s
print("The sum of cubes of first",n," natural number is:" , cubes(1,n))

#Sum of the Cubes from 11th to 40th
print("The sum of of cubes of 30 consecutive natural numbers starting from 11 is:", cubes(11,40))

