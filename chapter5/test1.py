class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def display(self):
        elements = []
        current = self.head
        while current is not None:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))


# Example usage:
if __name__ == "__main__":
    linked_list = LinkedList()
    # linked_list.append(5)
    # linked_list.append(10)
    # linked_list.append(15)
    # linked_list.prepend(2)
    # linked_list.delete(10)
    if linked_list.is_empty():
        print("Empty")
    linked_list.append(5)
    if linked_list.is_empty():
        print("Empty")
    linked_list.display()
