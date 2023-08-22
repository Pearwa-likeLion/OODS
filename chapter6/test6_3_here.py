def deleteIsland(Map,y,x): # position x , y of Map 
    #loop
    if x < 0:
        return
    else:
        print("y: ",y," x: ",x)
        print("Map: ",Map[y][x])
        if x==0 or x==len(Map)-1 and Map[y][x] == 1:
            pass
        return deleteIsland(Map,0,x-1)

def countIsland(Map):
    global count
    if len(Map) < 2:
        return count
    else:
        print("Map: ",Map)
        print("Map: ",Map[0])
        count += Map[0].count(1) 
        deleteIsland(Map,0,len(Map[0])-1)
        return countIsland(Map[1:])
    
        
Input = input("Enter Input : ").split('/')
Map=[]
count = 0

for i in Input:
    temp=[*i]
    temp = list(map(int,temp))
    Map.append(temp)

print(f"Island have : {countIsland(Map)}")
