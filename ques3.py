def menu():
    print("Enter 0 to convert feet inches")
    print("Enter 1 to convert feet centimeter")
    print("Enter 2 to convert feet millimeter")
    print("Enter 3 to convert feet meter")
    print("Enter 4 to convert feet kilometer")
    print("Enter 5 to convert feet yards")
    print("Enter 6 to convert feet miles")
feet=int(input("Enter height in feet"))
L=[]
L.append((12*feet,"inches"))
L.append(((12*feet*2.54),"centimeter"))
L.append(((12*feet*25.4),"millimeter"))
L.append(((12*feet*0.254),"meter"))
L.append(((12*feet*0.254*0.001),"kilometer"))
L.append(((feet/3),"yards"))
L.append(((feet/5280),"miles"))
menu()
a=int(input())
print(L[a])



