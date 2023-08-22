def deleteIsland(Map,y,x):
    if Map == []:
        return
    else:
        print()
        print("y:",y,"  x:",x)
        print(Map[0])
        return deleteIsland(Map[1:],len(Map)-1,len(Map)-1)

def countIsland(Map):
    if Map == []:
        return
    else:
        print(Map[0], end=" ")
        deleteIsland(Map[0],len(Map[0]),len(Map[0]))
        countIsland(Map[1:])
        
Input = input("Enter Input : ").split('/')
Map=[]

for i in Input:
    temp=[*i]
    temp = list(map(int,temp))
    Map.append(temp)

print(f"Island have : {countIsland(Map)}")
