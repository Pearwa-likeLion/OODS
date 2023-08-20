# จงเขียนฟังก์ชันเพื่อหาผลรวมของ 3 
# พจน์ใดๆใน Array ที่มีผลรวมเท่ากับ 0 
# สำหรับ Array ที่มีข้อมูลข้างในเป็นจำนวนจริง 
# ***Array ต้องมีความยาวตั้งแต่ 3 จำนวนขึ้นไป***
# Enter Your List : -25 -10 -7 -3 2 4 8 10
# [[-10, 2, 8], [-7, -3, 10]]
#_____________________________________________________#
num = input("Enter Your List : ").split(" ")
# print(len(num))
c = 0
l_num = len(num)
sum = 0
lst_arr = []
lst = []
logic = False
if len(num) < 3:
    print("Array Input Length Must More Than 2")
else:
    for x in range(0,l_num):
        if logic == True:
            break
        # print("time: "+str(c))
        for y in range(x+1,l_num,1):
            if logic == True:
                break
            for z in range(y+1,l_num,1):
                if logic == True:
                    break
                # print("time: "+str(c))
                # print("x: " + str(num[x]))
                # print("y: " + str(num[y]))
                # print("z: " + str(num[z]))
                sum = int(num[x]) + int(num[y]) + int(num[z])
                if sum == 0:
                    # print("x: " + str(num[x]))
                    # print("y: " + str(num[y]))
                    # print("z: " + str(num[z]))
                    lst.append(int(num[x]))
                    lst.append(int(num[y]))
                    lst.append(int(num[z]))
                    if lst in lst_arr: 
                        logic = True
                        break
                    else:
                        lst_arr.append(lst)
                    lst = []
        c += 1
    print(lst_arr)
