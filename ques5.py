"""are a student in a class of 10. Your class teacher assigns you a task of entering the
names of all the students in the class. You finally want to display the names given the
condition that the maximum allowed characters in a name is 15. As a fun task, reverse the
names and display them. [Hint: Slicing works when you are selecting maximum characters]"""
a=int(input("enter number of students:"))
L=[]
reverse_L=[]
for i in range(0,a):
    print("enter name of student",i+1)
    b=input()
    c=b[0:15]
    L.append(c)
for i in L:
    reverse_L.append(i[::-1])
    
print(L)
print(reverse_L)
      