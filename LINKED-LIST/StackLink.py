from Node import Node


class StackLink:
    def __init__(self):
        self.top=None
        
    def isEmpty(self):
        return self.top is None
    
    
    def push(self,data):
        new_node=Node(data)
        new_node.link=self.top
        self.top=new_node
        print(f"{data} is pushed")

    def pop(self):
        if self.isEmpty():
            print("Stack is underflow") 
        else:
            pop_data=self.top.data
            self.top=self.top.link
            print(f"{pop_data} is popped")
            return pop_data
        
        
    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        return self.top.data
    
    
    
    def display(self):
        if self.isEmpty():
            print("Stack is  empty")
            return
        current=self.top
        print("Top -->",end="")
        while current:
            print(current.data,end="-->")
            current=current.link
        print("None")
               
my_stack=StackLink()



while True:
    print("M E N U")
    print("1.P U S H")
    print("2.P O P")
    print("3.P E E K")
    print("4.D I S P L A Y")
    print("5.E X I T")

    choice=int(input("Enter your Choice: "))

    if choice==1:
        value=int(input("Enter value :"))
        my_stack.push(value)
    
    elif choice==2:
        my_stack.pop()

    elif choice==3:
        top_ele=my_stack.peek()
        print(f"Top is {top_ele}")

    elif choice==4:
        my_stack.display()


    elif choice==5:
        print("Exitting the program")
        exit()

