class Queue(object):
    def __init__ (self):
        self.item = []
    
    def push(self,item):
        self.item.append(item)
    # push the element into the list in the last index
        
    def pop(self):
        return self.item.pop(0)
        
    def peek(self):
        if self.item:
            return self.item[-1]
        else:
            return None
        
    def poptop(self,id):
        self.item[2:0] = id
        return self.item.pop(0)
        
    def size(self): 
        if self.item:
            return len(self.item)
        else:
            return None
        
    def isempty(self):
        if self.item == []:
            return True
        else:
            return False
        
q = Queue()
q.push("1")
q.push("2")
q.push("1")
q.push("5")
q.push("4")
q.push("1")
for i in q.item:
    print(i)
q.poptop("A")
for i in q.item:
    print(i)