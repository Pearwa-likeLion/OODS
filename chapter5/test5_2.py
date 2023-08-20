class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        if self.head == None:
            return True
        return False

    def append(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            current = self.head
            while current:
                current = current.next
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node
                        

    def addHead(self, item):
        #Code Here
        if self.head is None:
            self.append(item)
        else:
            new_node = Node(item)
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node

    def insert(self, pos, item):
        #Code Here
        count = 0
        new_node = Node(item)
        if self.head is None:
            self.addHead(item)
        elif pos > int(self.size()):
            self.append(item)
        elif pos < 0 and pos*-1 > int(self.size()):
            self.addHead(item)
        elif pos < 0:
            current = self.tail 
            count = 0
            while self.tail:
                if count == pos:
                    new_node.previous = current
                    new_node.next = current.next
                    if current.next:
                        current.next.previous = new_node
                    current.next = new_node
                    break
                current = current.previous
                count -= 1
        else:
            current = self.head
            while current:
                if pos-1 == count:
                    new_node.previous = current
                    new_node.next = current.next
                    if current.next:
                        current.next.previous = new_node
                    current.next = new_node
                    break
                current = current.next
                count += 1
            
    def search(self, item):
        #Code Here
        current = self.head
        while current:
            if current.value == item:
                return f"Found"
            current = current.next
        return "Not Found"

    def index(self, item):
        #Code Here
        count = 0
        current = self.head
        while current:
            if current.value  == item:
                return f"{count}"
            count += 1
            current = current.next
        return f"-1"

    def size(self):
        #Code Here
        count = 0
        current = self.head
        if current is None:
            return f"0"
        else:
            while current:
                count += 1
                current = current.next    
            return f"{count}"

    def pop(self, pos):
        #Code Here
        current = self.head
        count = 0
        if self.isEmpty():
            return f"Out of Range"
        while current:
            if pos == count:
                if current.previous:
                    current.previous.next = current.next
                else:
                    self.head = current.next
                
                if current.next:
                    current.next.previous = current.previous
                return f"Success"
            current = current.next
            count += 1
        return f"Out of Range"
                    
L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())


# Enter Input : PO -999,PO 999,PO 0,AP KMITL,PO 999,PO 0
# Out of Range | Empty
# Out of Range | Empty
# Out of Range | Empty
# Out of Range | KMITL 
# Success | KMITL -> Empty
# Linked List : Empty
# Linked List Reverse : Empty
