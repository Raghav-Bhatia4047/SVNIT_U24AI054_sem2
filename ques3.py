def utopian(n):
    a=1
    for i in range(1,n+1):
        if(i%2!=0):
            a=a*2
        else:
            a=a+1
    print(a)
test=int(input("Enter test cases "))
l=[]
for i in range(test):
    b=int(input("Enter number of cycles "))
    l.append(b)
    utopian(l[i]);