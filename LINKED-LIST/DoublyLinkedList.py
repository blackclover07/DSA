class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def create_list(self, elements):
        for elem in elements:
            self.add_last(elem)

    def display(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    def add_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_last(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp

    def add_after(self, target, data):
        temp = self.head
        while temp:
            if temp.data == target:
                new_node = Node(data)
                new_node.next = temp.next
                new_node.prev = temp
                if temp.next:
                    temp.next.prev = new_node
                temp.next = new_node
                return
            temp = temp.next
        print("Target node not found")

    def delete_first(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_last(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.prev.next = None

    def delete_middle(self, target):
        temp = self.head
        while temp:
            if temp.data == target:
                if temp.prev:
                    temp.prev.next = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                if temp == self.head:
                    self.head = temp.next
                return
            temp = temp.next
        print("Node not found")

dll = DoublyLinkedList()
while True:
    print("\nMenu:")
    print("1. Create Linked List")
    print("2. Display")
    print("3. Add at Beginning")
    print("4. Add at Last")
    print("5. Add After a Node")
    print("6. Delete First Node")
    print("7. Delete Last Node")
    print("8. Delete a Node from Middle")
    print("9. Exit")
    
    choice = int(input("Enter your choice: "))
    if choice == 1:
        elements = list(map(int, input("Enter elements separated by space: ").split()))
        dll.create_list(elements)
    elif choice == 2:
        dll.display()
    elif choice == 3:
        data = int(input("Enter data to insert at beginning: "))
        dll.add_beginning(data)
    elif choice == 4:
        data = int(input("Enter data to insert at last: "))
        dll.add_last(data)
    elif choice == 5:
        target = int(input("Enter the target node value: "))
        data = int(input("Enter data to insert after target: "))
        dll.add_after(target, data)
    elif choice == 6:
        dll.delete_first()
    elif choice == 7:
        dll.delete_last()
    elif choice == 8:
        target = int(input("Enter the node value to delete: "))
        dll.delete_middle(target)
    elif choice == 9:
        print("Exiting program...")
        break
    else:
        print("Invalid choice, please try again.")
