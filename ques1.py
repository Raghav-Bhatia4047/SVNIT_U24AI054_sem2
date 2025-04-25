class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None

    def End(self,data):
        new=node(data)
        if not self.head:
            self.head=new
        else:
            last=self.head
        while last.next!=None:
            last=last.next
        last.next=new
    def begin(self,data):
        new= node(data)
        if not self.head:
            self.head=new
        else:
            new.next=self.head
            self.head=new
    def display(self):
        if not self.head:
            print("print empty")
        else:
            current= self.head
            while current:
                print(current.data)
                current=current.next
    def delete(self):
        if not self.head:
            print("Empty")
        else:
            current=self.head
            prev=self.head
        while current.next!=None:
            current=current.next
            prev.next=current
        prev.next=None
        del(current)
    
def void():
    print("""Enter 
    0 to exit
    1 to insert at begin
    2 to insert at end
    3 to delete
    4 to display""")
L=Linkedlist()
while(1):
    void()
    k=int(input())
    match(k):
        case 0 : exit(1)
        case 1 :
                data=int(input("Enter data"))
                L.begin(data)
        case 2 : 
                data=int(input("enter data"))
                L.End(data)
        case 3 : 
                L.delete()
        case 4 : 
                L.display()
            

        

        



