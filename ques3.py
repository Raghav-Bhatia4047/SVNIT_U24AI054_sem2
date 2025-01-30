T=int(input("Enter number of Test cases:"))
for i in range(T):
   
    a=int(input("Enter the number: "))
    b=a
    count=0
    while(a!=0):
        c=a%10
        a=a//10
        if(b%c==0):
            count+=1
        else:
            continue
    print("number of position where digit exactly divides N:",count)
