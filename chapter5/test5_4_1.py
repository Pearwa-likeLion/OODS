class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.secondary_head = None

class Snode:
    def __init__(self, data):
        self.data = data
        self.next = None

class link:
    def __init__(self):
        self.head = None

    def next_node(self, data):
        new_node = node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                if current.data == new_node.data:
                    return
                current = current.next
            current.next = new_node

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def next_secondary_node(self, n, data):
        main_node = self.search(n)
        if main_node:
            if not main_node.secondary_head:
                main_node.secondary_head = Snode(data)
            else:
                current = main_node.secondary_head
                while current.next:
                    current = current.next
                current.next = Snode(data)

    def show_all(self):
        current = self.head
        while current:
            print(current.data, end=" : ")
            secondary_current = current.secondary_head
            while secondary_current:
                print(secondary_current.data, end=",")
                secondary_current = secondary_current.next
            print()
            current = current.next

inp = input("input : ").split(",")
l = link()

for i in inp:
    u = i.split(" ")
    if u[0] == "ADN":
        l.next_node(u[1])
    elif u[0] == "ADSN":
        h = u[1].split("-")
        l.next_secondary_node(h[0], h[1])

l.show_all()
