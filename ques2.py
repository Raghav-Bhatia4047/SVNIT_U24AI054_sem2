def fibonacci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

k=int(input("Enter the number"))
f=[]
i=0
a=0
while(a<k):
    a=fibonacci(i)
    i+=1
if(a==k):
    print("is fibo")
else:
    print("is not fibo")