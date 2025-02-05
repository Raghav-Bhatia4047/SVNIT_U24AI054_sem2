def digital(a):
    if(a<10):
        print(a) 
    else:
        sum=0
        while(a!=0):
            sum+=(a%10)
            a=a//10
        digital(sum)
a=int(input("Enter the number"))
digital(a)