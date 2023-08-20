# สมการ คือ จำนวน row and column = 2n + 4
# หาครึ่งนึง แถว n + 2
# คอลัม n + 2
# เช็ควงกลมเล็กของหยินหยาง โดยดูจากคอลัม โดนที่พิมพ์หยิงหยางไม่เกิน n หลังจากนั้นอีก 2 คอลัมพิมเครื่องหมายอย่างละเท่ากัน แล้วก็ทำลูปบนแต่กลับด้าน
# พิมพ์จุดเริ่มที่ n + 1 แล้วค่อยลดลงที่ละ 1 จนถึง 0 และ # เพิ่มขึ้นที่ละ 1 จนถึง n+2
# loop 2 รอบเพื่อให้ได้สี่เหลี่ยม คิดสมการข้างในต่อ
# Enter Input : 1
# ..#+++
# .##+#+
# ###+++
# ###+++
# #+#++.
# ###+..
# Enter Input : 2
# ...#++++
# ..##+##+ ||
# .###+##+ ||
# ####++++ == แบ่งเป็นครึ่งๆ
# ####++++ ==
# #++#+++. ||
# #++#++.. ||
# ####+...

#___________________________________________________#

n = int(input("Enter Input : "))
row_col = 2*n + 4
dot = n + 1
charp = 1
for row in range(row_col):
    if row <= n+1:
        for column in range(dot):
            print(".",end="")
        dot -= 1
        # print(charp)
        if charp <= n + 2:
            for column in range(charp):
                print("#",end="")
        charp += 1
        if row <= n +2:
            # for plus in range(n+2):
            if row == 0 or row == n + 1:
                plus = n+2
                print("+"*plus,end="")
            else:
                print("+",end="")
                print("#"*n,end="")
                print("+",end="") 
        print()
    if row > n +1:
        if row == n+2 or row == row_col-1:
            plus = n +2
            print("#"*plus,end="")
        else:
            print("#",end="")
            print("+"*n,end="")
            print("#",end="")
        if row >= n + 2:
            charp -= 1
            print("+"*charp,end="")
        if row >= n+2:
            dot += 1
            for column in range(dot):
                print(".",end="")
        print()
      
        