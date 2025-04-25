class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")
        self.display()

    def dequeue(self):
        if not self.is_empty():
            item = self.queue.pop(0)
            print(f"Dequeued: {item}")
            self.display()
            return item
        else:
            print("Queue is empty, cannot dequeue.")
            return None

    def is_empty(self):
        return len(self.queue) == 0

    def peek(self):
        if not self.is_empty():
            item= self.queue[0]
            self.display()
            print(item)
        else:
            print("Queue is empty.")
            return None

    def size(self):
        return len(self.queue)

    def display(self):
        print("Queue:", self.queue)
def void():
      print("""Enter 
    0 to exit
    1 to enqueue
    2 to dequeue
    3 to to check empty
    4 to display
    5 to check size
    6 to peek""")


q = Queue()
while(1):
    void()
    k=int(input())
    match(k):
        case 0 : exit(1)
        case 1 :
                data=int(input("Enter data: "))
                q.enqueue(data)
        case 2 : 
                q.dequeue()
        case 3 : 
                q.is_empty()
        case 4 : 
                q.display()
        case 5 : 
                q.size()
        case 6 :
                q.peek()
            

