from Node import Node


class QueueLink:
    def __init__(self):
        self.front=None
        self.rear=None
        
    def isEmpty(self):
        return self.front is None
    
    
    
    def enqueue(self,data):
        new_node=Node(data)
        if self.isEmpty():
            self.front=self.rear=new_node
        else:
            self.rear.link=new_node
            self.rear=new_node
            
        print(f"Enququed {data}")
        
    def dequeue(self):
        if self.isEmpty():
            print("Queue is in Underflow")
            return
        dequeue_data=self.front.data
        self.front=self.front.link
        if self.front is None:
            self.rear=None
        print(f"Dequeued {dequeue_data}")
        return dequeue_data
    
    def display(self):
        
        if self.isEmpty():
            print("Queue is empty")
            return
        current=self.front
        
        
        print("Front",end="-->")
        while current:
            print(current.data,end="-->")
            current=current.link
        print("None")
        
        
        
my_queue=QueueLink()

while True:
    print("M E N U")
    print("1.E N Q U E U E")
    print("2.D E Q U E U E")
    print("3.D I S P L A Y")
    print("4.E X I T")

    choice=int(input("Enter your Choice: "))

    if choice==1:
        value=int(input("Enter value :"))
        my_queue.enqueue(value)
    
    elif choice==2:
        my_queue.dequeue()

    elif choice==3:
        my_queue.display()

    elif choice==4:
        print("Exitting the program")
        exit()

