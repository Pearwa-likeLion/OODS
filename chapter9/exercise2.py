# def swap(l,biggest_i,biggest,start,stop):
#     if start == stop:
#         # print("recursion swap:",biggest_i)
#         return
#     else:
#         if l[start] > biggest:
#             biggest = l[start]
#             biggest_i = start
#         swap(l,biggest_i,biggest,start+1,stop)
#         return biggest_i
        

# def selection(l,last):
#     if last == 0:
#         return l
#     biggest = l[0]
#     biggest_i = 0
#     biggest_i = swap(l,biggest_i,biggest,1,last)
#     l[last] , l[biggest_i] = l[biggest_i] , l[last]
#     selection(l,last-1)
#     return l
    
# l = input("Enter Input : ").split(" ")
# n = len(l) - 1
# print(l)
# lst = selection(l,n)
# print("______________________________")
# print("After sorted: ",lst)


def selection(l):
    for last  in range(len(l)-1,0,-1):
        biggest = l[0]
        biggest_i = 0
        for i in range(1,last+1):
            if l[i] > biggest:
                biggest = l[i]
                biggest_i = i
        print()
        x = l[last]
        y = l[biggest_i]
        l[last] = y
        l[biggest_i] =  x
        print(f"sort : ",l)
        
l = input("Enter Input : ").split(" ")
n = len(l) - 1
print(l)
selection(l)
        

