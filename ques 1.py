a=int(input())
b=int(input())
max=a^b
zor = a^b
for i in range (a,b):
    for j in range(i,b+1):
        zor= i^j
        if(max<zor):
            max=zor

print (max)