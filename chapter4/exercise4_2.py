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

#PSD48
q = Queue()
count = 0 
c = 0
## =================== function for vip ==========================!!

def pushtop(fanclub):
    count = 0
    current_fanclub = fanclub.split(" ")[1]
    for f in q.item:
        id = f.split(" ")
        if id[0] == "ES":
            # print("id: ",id[1])
            count += 1
        elif id[0] == "EN":
            # print("id: ",id[1])
            break
    # print(count)
    return q.item.insert(count,fanclub)

## ======================== print ==========================!!

inp = input("Enter Input : ").split(",")
for ppl in inp:
    kind_fanclub = ppl.split(" ")
    if kind_fanclub[0] == "D":
        if q.isempty():
            print("Empty")
        else:
            # print("แสดงผลของหัวแถว")
            # display_id = q.pop()[1]
            display_id = q.pop().split(" ")[1]
            print(display_id)
    elif kind_fanclub[0] == "EN":
        # print("โอตะธรรมดา")
        # print(ppl)
        # print("EN: ",q.push(ppl))
        q.push(ppl)
        # p = q.push(kind_fanclub)
        # print(p)
    elif kind_fanclub[0] == "ES":
        if c == 0:
            q.item.insert(count,ppl)
            c+= 1
        else:
            # print("ES",pushtop(ppl))
            pushtop(ppl)
        # print(ppl)
        # print("โอตะของกองกำลังสำรวจ")
    # q.pop()


### นับจำนวน vip ไว้แล้ว insert เข้าไปใน list