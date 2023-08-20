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
        elif self.size() == 1:
            merge.append(self.head.value)
        else:
            cur, s = self.tail, str(self.tail.value) + " "
            merge.append(self.tail.value)
            while cur.previous != None:
                s += str(cur.previous.value) + " "
                merge.append(cur.previous.value)
                cur = cur.previous
            # return s
 

    def append(self, item):
        #Code Here
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                 current = current.next
            current.next = new_node
            new_node.previous = current
            self.tail = new_node
        # print(self.tail)
        
    def isEmpty(self):
        return self.head == None
    
    def size(self):
        #Code Here
        temp = self.head
        count = 0 
        if temp == None:
            return "Empty"
        while (temp) is not None:
            count += 1
            temp = temp.next
        return count
    
L1 = LinkedList()
L2 = LinkedList()
merge = LinkedList()
count = 0 

inp = input('Enter Input (L1,L2) : ').split(' ')
ll1 = inp[0].split("->")
ll2 = inp[1].split("->")
# print(ll1)
# print(ll2)

for i in ll1:
    L1.append(i)
    merge.append(i)
    
for j in ll2:
    L2.append(j)
    
print("L1    :",L1.__str__())
print("L2    :",L2.__str__())
L2.reverse()   
print("Merge :",merge.__str__())


    
