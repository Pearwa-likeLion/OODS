# n = int(input("Enter input : "))
# x = (4*n) -3
# z = 0
# y = 0
# for i in range(1,10):
#     if i%2 == 0:
#         for j in range(0,x):
#             # print(z)
#             if j %2 == 0 and j == z :
#                 print("#",end="")
#             else:
#                 print(".", end="")
#         z += 2
#         print("")
#     elif i%2 != 0 or i == 1 or i == x+1 :
#         for k in range(0,x):
#             print("#", end="")
#         print("")
#     print(i)
    
# for i in range(1,10):
#     if i%2 == 0:
#         for j in range(0,x):
#             # print(z)
#             if j %2 == 0 and j == z :
#                 print("#",end="")
#             else:
#                 print(".", end="")
#         z += 2
#         print("")
#     elif i%2 != 0 or i == 1 or i == x+1 :
#         for k in range(0,x):
#             print("#", end="")
#         print("")
#     print(i)
#_________________________________________________________________#
#################
#...............#
#.#############.#
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

#___________________________________________________________________#
n = int(input("Enter Input : "))
row_col = 2*n + 4
dot = -1
charp = 5
# for row in range(row_col):
#     if row <= n+1:
#         if row <= n +2:
#             # for plus in range(n+2):
#             if row == 0 or row == n + 1:
#                 plus = n+2
#                 print("#"*plus,end="")
#             else:
#                 print("#",end="")
#                 print("+"*n,end="")
#                 print("#",end="") 
#         if p >= 0:
#             for column in range(p-1):
#                 print("+",end="")
#         p -= 1
#         for column in range(dot+1):
#             print(".",end="")
#         dot += 1
#         # print(p)
#         print()
for row in range(row_col):
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
        
        
        
        
# ...#++++
# ..##+##+ ||
# .###+##+ ||
# ####++++ == แบ่งเป็นครึ่งๆ
# ####++++ ==
# #++#+++. ||
# #++#++.. ||
# ####+...