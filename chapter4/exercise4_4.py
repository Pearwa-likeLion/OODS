# ณ ร้านกาแฟแห่งหนึ่งมีบาริสต้า 2 คน จะมีลูกค้าเข้ามาในร้านเวลา (si) บาริสต้าจะทำกาแฟให้ลูกค้าแต่ละคนในเวลา (pi) ที่ต่างกัน ดังนั้นจะมีคนที่รอคิวอยู่ แสดงลำดับลูกค้าที่ได้กาแฟ และคนที่รอคิวเพื่อจะสั่งกาแฟนานที่สุดรอกี่นาที ถ้าไม่ต้องรอคิวเลยให้แสดง No waiting

# ตัวอย่างข้อมูลเข้า

# Log : 0,3/0,7/2,3/7,7/10,5/10,1

# คำอธิบาย

# ลูกค้าคนที่ 1 เข้ามาในเวลาที่ 0 และสั่งกาแฟที่ทำนาน 3 นาที 

# ลูกค้าคนที่ 2 เข้ามาในเวลาที่ 0 และสั่งกาแฟที่ทำนาน 7 นาที 

# ลูกค้าคนที่ 3 เข้ามาในเวลาที่ 2 และสั่งกาแฟที่ทำนาน 3 นาที 

# ลูกค้าคนที่ 4 เข้ามาในเวลาที่ 7 และสั่งกาแฟที่ทำนาน 7 นาที 

# ลูกค้าคนที่ 5 เข้ามาในเวลาที่ 10 และสั่งกาแฟที่ทำนาน 5 นาที 

# ลูกค้าคนที่ 6 เข้ามาในเวลาที่ 10 และสั่งกาแฟที่ทำนาน 1 นาที 

# ไทม์ไลน์

# เวลา(t)    เหตุการณ์

# 0    ลูกค้าคนที่ 1 และ 2 เข้ามาในร้านและสั่งกาแฟ

# 2    ลูกค้าคนที่ 3 เข้ามาในร้าน

# 3    ลูกค้าคนที่ 1 ได้กาแฟ ลูกค้าคนที่ 3 สั่งกาแฟหลังจากรอคิวไป 1 นาที

# 6    ลูกค้าคนที่ 3 ได้กาแฟ

# 7    ลูกค้าคนที่ 2 ได้กาแฟ ลูกค้าคนที่ 4 เข้ามาในร้านและสั่งกาแฟ

# 10    ลูกค้าคนที่ 5 และ 6 เข้ามาในร้าน ลูกค้าคนที่ 5 สั่งกาแฟ

# 14    ลูกค้าคนที่ 4 ได้กาแฟ ลูกค้าคนที่ 6 สั่งกาแฟหลังจากรอคิวไป 4 นาที

# 15    ลูกค้าคนที่ 5 และ 6 ได้กาแฟ

# ผลลัพธ์ 

# Time 3 customer 1 get coffee  

# Time 6 customer 3 get coffee  

# Time 7 customer 2 get coffee  

# Time 14 customer 4 get coffee  

# Time 15 customer 5 get coffee  

# Time 15 customer 6 get coffee  

# The customer who waited the longest is : 6

# The customer waited for 4 minutes


# เทียบ size ของ queue ว่าตอนนึ้ <= 2 มั้ยถ้าใช่ก็อย่าพึ่งทำ

class Queue:
  def __init__(self):
    self.queue = []

  def enqueue(self, item):
    self.queue.append(item)

  def dequeue(self):
    return self.queue.pop(0)

  def is_empty(self):
    return self.queue == []

  def size(self):
    return len(self.queue)


def cafe(log):
  queue = Queue()
  barista_1_time = barista_2_time = 0
  max_time = 0
  customer_wait = 0
  current_index = 0
  customer_list = []

  for item in log:
    queue.enqueue([int(item[0]), int(item[1])])

  while not queue.is_empty():
    current_index += 1
    current_customer = queue.dequeue()
    if barista_1_time >= barista_2_time and current_customer[0] <= barista_1_time:
      barista_1_time, barista_2_time = barista_2_time, barista_1_time
    if current_customer[0] > barista_1_time:
      barista_1_time = current_customer[0]

    if max_time < barista_1_time - current_customer[0]:
      max_time = barista_1_time - current_customer[0]
      customer_wait = current_index
    barista_1_time += current_customer[1]

    customer_list.append([barista_1_time, current_index])

  customer_list.sort()

  for customer in customer_list:
    print(f'Time {customer[0]} customer {customer[1]} get coffee')

  if customer_wait == 0 and max_time == 0:
    print('No waiting')
  else:
    print(f'''The customer who waited the longest is : {customer_wait}
The customer waited for {max_time} minutes''')


if __name__ == '__main__':
  print(" ***Cafe***")
  log = [i.split(',') for i in input('Log : ').split("/")]

  cafe(log)


