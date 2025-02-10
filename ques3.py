a=set()
str=input("Enter the string: ")
str=str.lower()
for i in str:
    if(i.isalpha()):
        a.add(i)
if(len(a)==26):
    print("pangram")
else:
    print("not a pangram")