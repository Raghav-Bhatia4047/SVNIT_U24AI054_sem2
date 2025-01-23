a = int(input("Enter max height:"))
b=[]
count=0
for i in range(0,a):
    c = int(input("Enter height of person"))
    b.append(c)
for i in range(0,a):
    min=b[i]
    index=i
    for j in range(i+1,a):
        if(min>b[j]):
            min=b[j]
            index=j
    if(i!=index):
            temp=b[i]
            b[i]=b[index]
            b[index]=temp
            count+=1
    else:
            continue
print(b)
print(count)

