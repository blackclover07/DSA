class Node:
    def __init__(self, coeff, power):
        self.coeff = coeff
        self.power = power
        self.next = None

class Polynomial:
    def __init__(self):
        self.head = None

    def insert_term(self, coeff, power):
        new_node = Node(coeff, power)
        if not self.head or self.head.power < power:
            new_node.next = self.head
            self.head = new_node
            return
        
        temp = self.head
        while temp.next and temp.next.power > power:
            temp = temp.next
        
        if temp.next and temp.next.power == power:
            temp.next.coeff += coeff  # Combine like terms
        else:
            new_node.next = temp.next
            temp.next = new_node

    def display(self):
        if not self.head:
            print("Polynomial is empty.")
            return
        
        temp = self.head
        poly_str = ""
        while temp:
            if temp.coeff != 0:
                poly_str += f"{'+' if temp.coeff > 0 and temp != self.head else ''}{temp.coeff}x^{temp.power} "
            temp = temp.next
        print("Polynomial:", poly_str.strip())

    def derivative(self):
        if not self.head:
            print("Polynomial is empty.")
            return

        print("Derivative:")
        temp = self.head
        while temp:
            if temp.power != 0:
                print(f"{temp.coeff * temp.power}x^{temp.power - 1}", end=" ")
            temp = temp.next
        print()


# Main program execution
poly = Polynomial()
while True:
    print("\nMENU:")
    print("1. Create Polynomial")
    print("2. Display Polynomial")
    print("3. Derivative of Polynomial")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        n = int(input("Enter the number of terms: "))
        for _ in range(n):
            coeff = int(input("Enter coefficient: "))
            power = int(input("Enter power: "))
            poly.insert_term(coeff, power)

    elif choice == 2:
        poly.display()

    elif choice == 3:
        poly.derivative()

    elif choice == 4:
        print("Exiting...")
        break
    
    else:
        print("Invalid choice! Please try again.")
