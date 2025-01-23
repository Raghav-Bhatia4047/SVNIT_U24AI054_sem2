import random
number=[]
for i in range(100):
    number.append(random.randint(0,1))
print(number)
count=0
max=0
for i in range(100):
    if(number[i]== 0):
        count+=1
    else:
        if(max<count):
            max=count
        count=0
print(max)