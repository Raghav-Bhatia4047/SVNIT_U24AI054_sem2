T=int(input("Enter test cases: "))
for i in range(T):
    str=input("Enter string: ")
    a=len(str)
    sum=0
    for i in range (len(str)//2):
        sum+=(max(ord(str[i]),ord(str[0-i-1]))-min(ord(str[i]),ord(str[0-i-1])))
    print(sum)
