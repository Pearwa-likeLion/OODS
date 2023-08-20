# จงเขียนฟังก์ชันเพื่อหาผลรวมของ 3 พจน์ใดๆใน Array ที่มีผลรวมเท่ากับ 0 สำหรับ Array 
# ที่มีข้อมูลข้างในเป็นจำนวนจริง ***Array ต้องมีความยาวตั้งแต่ 3 จำนวนขึ้นไป***
# Enter Your List : -25 -10 -7 -3 2 4 8 10
# [[-10, 2, 8], [-7, -3, 10]]
#________________________________________________________________________#
# num = input("Enter Your List : ").split(" ")
# c = 0
# l_num = len(num)
# for x in range(0,l_num):
#     # print("time: "+str(c))
#     print(x)
#     for y in range(-1,l_num,1):
#         print(y)
#         for z in range(2,l_num,1):
#             print("time: "+str(c))
#             print(z)
#             # print("x: " + str(num[x]))
#             # print("y: " + str(num[y]))
#             # print("z: " + str(num[z]))
#     c += 1
def most_repeating_word(strg):
    words =strg.split()
    max_repeat_count = 0
    for words1 in words:
        dict1 = {}
        for letter in words1:
            if letter not in dict1:
                dict1[letter] = 1
            else:
                dict1[letter] += 1
            if dict1[letter]> max_repeat_count:
                max_repeat_count = dict1[letter]
                most_repeated_char = letter
                result=words1
    return result
print(most_repeating_word('ball'))