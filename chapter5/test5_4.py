class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Create a linked list of linked lists
outer_linked_list = LinkedList()

inner_list1 = LinkedList()
inner_list1.append(1)
inner_list1.append(2)
inner_list1.append(3)

inner_list2 = LinkedList()
inner_list2.append(4)
inner_list2.append(5)

outer_linked_list.append(inner_list1)
outer_linked_list.append(inner_list2)

# Display the structure
current = outer_linked_list.head
while current:
    inner_list = current.data
    inner_list.display()
    current = current.next
    print("Outer List Next")
