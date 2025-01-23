T=int(input("Enter number of test cases:"))
for i in range(1,T+1,1):
    n=int(input("enter number of boxes:"))
    x=int(input("enter number of box in which coin is placed:"))
    s=int(input("enter number of swaps:"))
    L=[0]
    for i in range(0,n,1):
        L.append(0)
    L[x-1]=1
    for i in range(1,s+1,1):
        print("ente boxes to swap")
        a=int(input("enter box A:"))-1
        b=int(input("enter box B:"))-1
        c=L[a]
        L[a]=L[b]
        L[b]=c
    for i in range(0,n,1):
        if (L[i]==1):
            print("coin in box ",i+1,sep='')
        else:
            continue 