# Original unsorted list
unsorted_list = input("Enter input: ").split(",")
unsorted_list = [eval(i) for i in unsorted_list]
# Bubble sort implementation
for i in range(len(unsorted_list)-1,0,-1):
    print("i: ",i)
    for j in range(len(unsorted_list)-i-1,-1,-1):
        print("j: "+str(j))
        print(f"{unsorted_list[j]}  {unsorted_list[j+1]}")
        if unsorted_list[j] < unsorted_list[j+1]:
            temp = unsorted_list[j]
            unsorted_list[j] = unsorted_list[j+1]
            unsorted_list[j+1] = temp

# Print the sorted list
print(unsorted_list) # Output: [1, 2, 3, 5, 8]

