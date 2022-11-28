#Prime Numbers
def prime(n):
    l=[i for i in range (2,n+1)]
    for j in l:
        for k in range (2,n+1):
            if j*k in l:
                l.remove(j*k)
    return l
print("Prime numbers till 200 is :", prime(200))


