# def sort(lst,m):
#     if m == 0:
#         return lst
#     else:
#         print("m: ",m)
#         if lst[m] < lst[m-1]:
#             temp = lst[m]
#             lst[m] = lst[m+1]
#             lst[m+1] = temp
#         return sort(lst,m-1)

# def sortedNumber(lst,n):
#     # x = len(lst) -1
#     if n == 0:
#         return lst
#     else:
#         # n+=1
#         return sortedNumber(lst,n-2)
    

# unsorted_list = input("Enter input: ").split(",")
# lst = [eval(i) for i in unsorted_list]
# n = len(lst) - 1
# sortedNumber(lst,n)
# print(lst)


def resorted(lst,n):
    pass

def bubble_sort_recursive(arr, n):
    if n == 0:
        return
    
    for i in range(len(arr)-n,n,1):
        # print(i)
        if arr[i] < arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    return bubble_sort_recursive(arr, n - 1)

# Original unsorted list
unsorted_list = input("Enter input: ").split(",")
unsorted_list = [eval(i) for i in unsorted_list]

# Call the recursive function
bubble_sort_recursive(unsorted_list, len(unsorted_list))

# Print the sorted list
print(unsorted_list)
