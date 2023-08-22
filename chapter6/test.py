def reverse_sort_list(lst):
    n = len(lst)
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

# Example list
my_list = input("Enter input: ").split(",")
my_list = [eval(i) for i in my_list]
print("Original list:", my_list)

reverse_sort_list(my_list)
print("Sorted in descending order:", my_list)
