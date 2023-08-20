class Node:
    def __init__(self,data,next = None):
        self.data = data
        if next is None:
            self.next = None
        else:
            self.next = next
            
    
class linkedList:
    def __init__(self):
        self.head = None
        
    # เพิ่ม data ต่อท้าย linked list
    def append(self,data):
        p = Node(data)
        if self.head == None:
            self.head = p
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = p
    
    #create new node
    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node 
    
    #return string แสดง linked list 
    def __str__(self) -> str:
        display = []
        current = self.head
        while current is not None:
            display.append(current.data)
            current = current.next
        print("link list : ",end= "")
        print("->".join(map(str, display)))
    
    # return list is it Empty?
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
    
    #insert data ใน index ที่กำหนด
    def insert(self,index,data):
        if index == 0 :
            print(f"index = {index} and data = {data}")
            self.prepend(data)
            self.__str__()
        elif index < 0 :
             print("Data cannot be added")
             self.__str__()
        else:
            new_node = Node(data)
            current = self.head
            count = 1
            while current is not None and count < index:
                current = current.next
                count += 1
            if current is None:
                print("Data cannot be added")
                if  self.head == None:
                    print("List is empty")
                else:
                    self.__str__()
            else:
                print(f"index = {index} and data = {data}")
                new_node.next = current.next
                current.next = new_node
                self.__str__()
if __name__ == "__main__":
    linked_list = linkedList()
    inp = input("Enter Input : ").split(",")
    d = inp[0].split(" ")
    if inp[0] == '':
        print("List is empty")
    else:
        for i in d:
            linked_list.append(i)
        linked_list.__str__()
    for data in inp[1:]:
        data_split = data.split(":")
        linked_list.insert(int(data_split[0]),data_split[1])        
