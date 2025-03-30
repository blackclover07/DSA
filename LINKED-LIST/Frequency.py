class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def count_frequencies(self):
        freq_dict = {}
        current = self.head
        while current:
            freq_dict[current.data] = freq_dict.get(current.data, 0) + 1
            current = current.next
        return freq_dict

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example Usage
llist = LinkedList()
numbers = [3, 2, 3, 1, 2, 3, 4, 1]
for num in numbers:
    llist.insert(num)

llist.display()
freqs = llist.count_frequencies()
print("Frequencies:", freqs)
