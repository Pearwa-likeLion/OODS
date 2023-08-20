# รับ input 1 บรรทัด โดย แต่ละลำดับ จะมีอักษรกำกับไว้และตามด้วยจำนวนครั้งที่ต้องทำตามตัวอักษรนั้น 
# E คือ การ enqueue และ D คือการ dequeue แต่หากเป็นตัวอักษรอื่นให้นับเป็น error input
# ต้องบอกว่า มีการ dequeue ที่ไม่เกิดผลกี่ครั้งตามลำดับ และแต่ละครั้งที่มีการเกิดขึ้นใน Queue 
# มีการเปลี่ยนแปลงอย่างไรตามขั้นตอน
# รับ input 1 บรรทัด โดย แต่ละลำดับ จะมีอักษรกำกับไว้และตามด้วยจำนวนครั้งที่ต้องทำตามตัวอักษรนั้น 
# E คือ การ enqueue และ D คือการ dequeue แต่หากเป็นตัวอักษรอื่นให้นับเป็น error input
# ต้องบอกว่า มีการ dequeue ที่ไม่เกิดผลกี่ครั้งตามลำดับ และแต่ละครั้งที่มีการเกิดขึ้นใน Queue 
# มีการเปลี่ยนแปลงอย่างไรตามขั้นตอน
class Queue:
    def __init__(self, list= None):
        self.item = []

    
    def enQueue(self,items):
        self.item.append(items)
        
    def deQueue(self):
        return self.item.pop(0)   
    
    def isEmpty(self):
        if self.item == []:
            return True
        else: False
        
    def size(self):
        return len(self.item)

q = Queue()
count_e = 0
error = 0
count_d = 0
err_inp = 0
inp = input("input : ")
lst = inp.split(",")
for item in lst:
    if item[0] == "E":
        print("Step :",item)
        num_e = int(item[1:])
        if str(num_e).isdigit():
            for i in range(count_e,count_e+num_e,1):
                count_e += 1
                q.enQueue(str("*"+str(i)))
            print("Enqueue :",q.item)
        else:
            err_inp += 1
    elif item[0] == "D":
        num_d = int(item[1:])
        print("Step :",item)
        if str(num_d).isdigit():
            if q.isEmpty():
                error += num_d
            else:
                for j in range(num_d):
                    if q.isEmpty():
                        break
                    else:
                        q.deQueue()
                        count_d += 1
                error = (num_d - count_d) + error
            print("Dequeue :",q.item)
        else:
            err_inp += 1
    else:
        print("Step :",item)
        print(q.item)
        err_inp += 1
    print("Error Dequeue :",error)
    print("Error input :",err_inp)
    print("--------------------")

# --------------------
# --------------------