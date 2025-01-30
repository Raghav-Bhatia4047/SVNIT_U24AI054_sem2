L=input("Enter a word: ")
Q=""
for i in range(0,len(L),1):
    if((i%2)==0):
       Q=Q+L[i]
    else:
        Q=Q+L[i].upper()
print(Q)

