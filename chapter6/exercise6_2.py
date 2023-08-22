def sortedNumber(unsortedList,sortedList,n):
    if unsortedList == []:
        return unsortedList
    else:
        # print(unsortedList)
        maxnum = max(unsortedList)
        sortedList.append(maxnum)
        unsortedList.remove(maxnum)
        return sortedNumber(unsortedList,sortedList,n-1)
        
lst = input("Enter your List : ")
sortedList = []
unsortedList = list(map(int, lst.split(",")))
# print(unsortedList)
n = len(lst)
sortedNumber(unsortedList,sortedList,n)
print("List after Sorted :",sortedList)