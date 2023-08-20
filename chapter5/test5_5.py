# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# def getMax(arr):
#     max_val = arr[0]
#     for num in arr:
#         if num > max_val:
#             max_val = num
#     return max_val

# def countSort(arr, exp):
#     output = [0] * len(arr)
#     count = [0] * 10

#     for num in arr:
#         index = (num // exp) % 10
#         count[index] += 1

#     for i in range(1, 10):
#         count[i] += count[i - 1]

#     i = len(arr) - 1
#     while i >= 0:
#         num = arr[i]
#         index = (num // exp) % 10
#         output[count[index] - 1] = num
#         count[index] -= 1
#         i -= 1

#     for i in range(len(arr)):
#         arr[i] = output[i]

# def radixSort(arr):
#     max_val = getMax(arr)
#     exp = 1
#     while max_val // exp > 0:
#         countSort(arr, exp)
#         exp *= 10

# def printList(node):
#     while node:
#         print(node.data, end=" -> ")
#         node = node.next
#     print("None")

# def radixSortLinkedList(head):
#     arr = []
#     current = head
#     while current:
#         arr.append(current.data)
#         current = current.next
    
#     radixSort(arr)
    
#     current = head
#     for num in arr:
#         current.data = num
#         current = current.next

# # Creating the linked list from the input values
# input_values = input("Enter input: ").split(" ")
# input_values = [eval(i) for i in input_values]
# head = Node(input_values[0])
# current = head
# for val in input_values[1:]:
#     current.next = Node(val)
#     current = current.next

# print("Before Radix Sort:", end=" ")
# printList(head)

# radixSortLinkedList(head)

# print("After Radix Sort:", end=" ")
# printList(head)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def getMax(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

def countSort(arr, exp):
    output = [0] * len(arr)
    count = [0] * 10

    for num in arr:
        index = (num // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = len(arr) - 1
    while i >= 0:
        num = arr[i]
        index = (num // exp) % 10
        output[count[index] - 1] = num
        count[index] -= 1
        i -= 1

    for i in range(len(arr)):
        arr[i] = output[i]

def radixSort(arr):
    max_val = getMax(arr)
    exp = 1
    while max_val // exp > 0:
        countSort(arr, exp)
        exp *= 10

def printList(node):
    while node:
        print(node.data, end=" -> ")
        node = node.next
    print("None")

def radixSortLinkedList(head):
    arr = []
    current = head
    while current:
        arr.append(current.data)
        current = current.next
    
    radixSort(arr)
    
    current = head
    for num in arr:
        current.data = num
        current = current.next

# Creating the linked list from the input values
input_values = [-1, -9, -3, -6, -5, -4, -7, 0, -8, -2, 3, 2, 5, 1, 4, 9, 8, 7, 6]
head = Node(input_values[0])
current = head
for val in input_values[1:]:
    current.next = Node(val)
    current = current.next

print("Before Radix Sort:", end=" ")
printList(head)

radixSortLinkedList(head)

print("After Radix Sort:", end=" ")
printList(head)
