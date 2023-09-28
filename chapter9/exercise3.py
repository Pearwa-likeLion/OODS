def maxtoMin(l):
    for i in range(len(l)-1):
        for j in range(len(l)-1):
            if l[j] < l[j+1]:
                l[j] , l[j+1] = l[j+1] , l[j]
    return l            

def mintoMax(l):
    for i in range(len(l)-1):
        for j in range(len(l)-1):
            if l[j] > l[j+1]:
                l[j] , l[j+1] = l[j+1] , l[j]
    return l

def checkDuplicate(l):
    d = {}
    logic = False
    for w in l:
        if w in d.keys():
            d[w] += 1
            logic = True
            
        else:
            d[w] = 0
    if len(d) == 1:
        return f"Dupli"
    elif logic == True:
        return logic
    else: return logic

inp = input("Enter Input : ")

l = []
for w in inp:
    l.append(w) 
defult = l.copy()

max = maxtoMin(l.copy())
min = mintoMax(l.copy())
check = checkDuplicate(l)

if check == "Dupli":
    print("Repdrome")
elif l == min and check == False:
    print("Metadrome")
elif l == min and check == True:
    print("Plaindrome")
elif defult == max and check == False:
    print("Katadrome")
elif l == max and check == True:
    print("Nialpdrome")
else:
    print("Nondrome")