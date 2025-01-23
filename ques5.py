n = int(input("Enter the number: "))
a=0
while(n>0):
    a= (a*10)+(n%10)
    n=n//10
print("reverse of that number is",a)