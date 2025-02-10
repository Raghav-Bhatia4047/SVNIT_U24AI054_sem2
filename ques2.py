T=int(input())
for i in range(T):
    A=input()
    A=A.split
    a,b=int(A[1]),int(A[2])
    c,d=int(a**0.5),int(b**0.5)
    if((c**2)>=a and (d**2)<=b):
        print(d-c+1)
    else:
        print(d-c)
