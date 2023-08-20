class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def pop(self):
        if self.head is None:
            return None  # The list is empty

        if self.head == self.tail:
            # The list has only one node
            data = self.head.data
            self.head = None
            self.tail = None
            return data

        data = self.tail.data
        self.tail = self.tail.prev
        self.tail.next = None
        return data

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" <-> ".join(str(data) for data in elements))

# Example usage:
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.prepend(0)

    print("Original list:")
    dll.display()  # Output: 0 <-> 1 <-> 2 <-> 3

    last_node_data = dll.pop()
    print(f"\nPopped data: {last_node_data}")
    dll.display()  # Output: 0 <-> 1 <-> 2
