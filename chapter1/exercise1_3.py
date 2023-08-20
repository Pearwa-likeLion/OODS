# โรงเรียนดังประจำจังหวัดแห่งหนึ่ง จะมีการจัดการเลือกตั้งหาประธานนักเรียนคนใหม่ขึ้นในทุกๆปี โดยในปีนี้มีผู้เข้าแข่งขันสูงถึง 20 คน 
# โดยกฤษฎาได้รับมอบหมายให้เป็นผู้นับคะแนนเลือกตั้งในปีนี้ แต่กฤษฎารู้สึกขี้เกียจนับคะแนนขึ้นมา จึงได้ไหว้วานให้คุณช่วยเขียนโปรแกรม 
# ในการหาว่าผู้เข้าแข่งขันคนใดได้รับคะแนนสูงที่สุด
# ข้อควรระวัง หากมีการเลือกเลขที่ไม่ตรงกับผู้เข้าแข่งขัน (1-20) จะนับว่าเป็นบัตรเสีย และถ้าหากทุกใบเป็นบัตรเสียจะถือว่าไม่มีผู้ชนะ

#________________________________________________________________________________________________________#

print("*** Election ***")
election = {}
x= int(input("Enter a number of voter(s) : "))
num = input().split()
ln = len(num)
#dict
while ln > 0:
    election[num[ln-1]] = int(0)
    ln -= 1

#calculation
for n in num:
    if int(n) < 0 or int(n) > 20:
        election[n] = 0 
        continue
    elif n in election.keys():
        election[n] += 1
# print(election)
c = 0
lst =[]
max_value = max(election, key=election.get)
for i in election.keys():
    if election[i] == election[max_value] and election[max_value] != 0:
        c += 1
        lst.append(i)
if c == 0:
    if election[max_value] == 0:
        print("*** No Candidate Wins ***")
    else:
        print(max_value)
else:
    for i in lst : print(i , end= " ")