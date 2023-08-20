n = int(input("Enter input : "))
odd = 4 #0
even  = 4 #0
x = 4*n - 3
dot_odd = 1 #x
dot_even = 1 #x
#แบ่งบรรทัดคี่คูู่
for row in range(10,x+1):
    if row%2 == 0:
        # print("."*x,end="")
        for i in range(odd):
            print("#.",end="")
        print("."*dot_odd,end="")
        dot_odd += 4
        for j in range(odd):
            print(".#",end="")
        odd -= 1
    elif row%2 != 0:
        for i in range(even-1):
            print("#.",end="")
        dot_even += 4
        print("#"*dot_even,end="")
        for j in range(even-1):
            print(".#",end="")
        even -= 1
    print()

#.#.#.#...#.#.#.#
#.#.#.#####.#.#.#
#.#.#.......#.#.#
#.#.#########.#.#
#.#...........#.#
#.#############.#
#...............#
#################