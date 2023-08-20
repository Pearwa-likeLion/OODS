# *** Fun with Drawing ***
# Enter input : 5
# condition ใช้ ตำแหน่งเป็นเงื่อนไขในการเปลี่ยนเครื่องหมายการพิมพ์ และตำแหน่งจะขยับก็ต่อเมื่อเปลี่ยนไปเป็นบรรทัดถัดไปที่มี patern เดียวกัน

################# 
#...............# เพิ่ม # ที่ละ 1 หน้าหลัง และเพิ่มแบบเว้นวรรคตำแหน่งเป็นจำนวนคี่ อาจจะใช้การวนลูปสองรอบ row และ colum โดย colum ของอันนี้จะวน ตำแหน่งที่จะวาด # แล้วพอไม่ใช่ตำแหน่งที่วาด # ก็จะวาดจุดยาว
#.#############.# ทำเหมือนข้างบนแต่พิมพ์ . ที่ตำแหน่งคู่ โดยจะนับ 1 ที่ตำแหน่งนี้ พิมพ์หน้าหลังแล้วถ้าเกินความยาวตำแหน่งก็ให้ ย้ายไปพิมพ์ # แทน  
#.#...........#.#
#.#.#########.#.#
#.#.#.......#.#.#
#.#.#.#####.#.#.#
#.#.#.#...#.#.#.#
#.#.#.#.#.#.#.#.#
#.#.#.#...#.#.#.#
#.#.#.#####.#.#.#
#.#.#.......#.#.#
#.#.#########.#.#
#.#...........#.#
#.#############.#
#...............#
#################

#_____________________________________________________________________________________________#
print("*** Fun with Drawing ***")
n = int(input("Enter input : "))
odd = 0
even  = 0
x = 4*n - 3
dot_odd = x
dot_even = x
#แบ่งบรรทัดคี่คูู่
for row in range(x+1):
    if row == (int((x-1)/2)+1):
        continue
    if row%2 == 0:
        if row == 0 :
            print("#"*x,end="")
        elif row >= int((x-1)/2)+2:
            for i in range(odd):
                print("#.",end="")
            print("."*dot_odd,end="")
            dot_odd += 4
            for j in range(odd):
                print(".#",end="")
            odd -= 1
        else:
            for column in range(x):
                if column <= even and row%2 == 0:
                    print("#",end="")
                    print(".",end="")
                else:
                    dot_even = x - (row*2)
                    print("#"*dot_even,end="")
                    break
            for d in range(even+1):
                print(".",end="")
                print("#",end="")
            even += 1
    elif row%2 != 0:
        # print(row)
        if row >= int((x-1)/2)+2:
            for i in range(even-1):
                print("#.",end="")
            dot_even += 4
            print("#"*dot_even,end="")
            for j in range(even-1):
                print(".#",end="")
            even -= 1
        else:
            for column in range(x):
                if column <= odd and row%2 != 0:
                    print("#",end="")
                    print(".",end="")
                else:
                    dot_odd = x - (row*2) - 2
                    print("."*dot_odd,end="")
                    break
            for d in range(odd+1):
                print(".",end="")
                print("#",end="")
            odd += 1
    print()