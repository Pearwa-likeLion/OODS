class Node:
    def __init__(self,data):
        self.data = data
        self.secondary_head = None
        self.next = None

class Snode:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self) -> None:
        self.head = None
    
    def next_node(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head =  new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def seach(self,data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        current.next = current
        return None
    def secondary_node(self,n,data):
        main_node = self.seach(n)
        if main_node:
            if main_node.secondary_head is not None:
                main_node.secondary_head = Snode(data)
                
            else:
                current = main_node.secondary_head
                while current:
                    print(current.data , end=" ")
                    current = current.next
                print()
                current = current.next

    def __str__(self):
        curr = self.head
        while curr:
            print(curr.data, end=" : ")
            secondnode = curr.secondary_head
            while secondnode:
                print(secondnode.data , end=" ")
                secondnode = secondnode.next
            print()         
            curr = curr.next
            
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
            
def get_max_digit(n):
    i = 0
    max_d = 0
    for j in n:
        x= int(j)
        if x < 0:
            x = x * -1
        while x > 0:
            x //= 10
            i += 1
        if i > max_d:
            max_d = i
        i= 0
    return max_d


inp = input("Enter Input : ").split(" ")
max_digit = get_max_digit(inp)       
index = 0          
# print(max_digit)
l = linkedList()
for i in range(0,10):
    l.next_node(str(i))
for index in range(1,1+max_digit):
    print("------------------------------------------------------------")
    print("Round : ",index)
    l.show_all()
    
print(f"{index} Time(s)")
print(f"Before Radix Sort :", " -> ".join(inp))
# 3 Time(s)
# Before Radix Sort : 64 -> 8 -> 216 -> 512 -> 27 -> 729 -> 0 -> 1 -> 343 -> 125
# After  Radix Sort : 0 -> 1 -> 8 -> 27 -> 64 -> 125 -> 216 -> 343 -> 512 -> 729

