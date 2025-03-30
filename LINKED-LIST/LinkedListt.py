from Node import Node
        
class LinkedListt:
    # consructor 
    def __init__(self):
        self.head=None #initializes the head as Node
        
      
    # Funcion to Create a Node in linked list  
    def createNode(self,data):
        p=self.head   # Assingning the p as head to use a pointer replica 
        q=Node(data)  
        
        if p==None:    
            self.head=q
        else:
            while p.link != None:
                p=p.link
            p.link=q
        
    # Function to display the linked list
    def displayList(self):
        p=self.head  # Assingning the p as head to use a pointer replica 
        if p==None:
            print("list is empty")
        while p!= None:
            print(p.data,end="")
            if p.link!=None:
                print(" -->",end="")
            p=p.link
            
    def addBegin(self,data):
        p=self.head
        q=Node(data) 
        if p==None:
            self.head=q
        else:
            q.link=p
            self.head=q    
    def addBetween(self,data,target):
        p=self.head
        q=Node(data)
        
        if p==None:
            self.head=q
        else :
            while p.link!=None:
                if p.data==target:
                    q.link=p.link
                    p.link=q
                p=p.link
my_list=LinkedListt()

while True:
    print()
    print("M A I N M E N U")
    print("1.Create Node")
    print("2.Display")
    print("3.Add Node at the Begin")
    print("4.Add Node at the Between")
    print("9.Exit")
    
    choice=int(input("Enter choice : "))
    
    if choice==1:
        val=int(input("Enter value : "))
        my_list.createNode(val)
    if choice==2:
        my_list.displayList()
    
    if choice==3:
        val=int(input("Enter Value : "))
        my_list.addBegin(val)
    
    if choice==4:
        val=int(input("Enter Value : "))
        target =int(input("Enter target : "))
        my_list.addBetween(val,target)
    if choice==9:
        exit()
    
    
        