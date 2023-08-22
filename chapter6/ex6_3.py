def deleteIsland(Map,y,x):
    row_index = y
    col_index = x
    Map[row_index][col_index] = 0
    
    #go left
    if col_index > 0:
        if Map[row_index][col_index-1] == 1:
            deleteIsland(Map,row_index,col_index-1)
    #go right 
    if len(Map[row_index]) > col_index+1:
        if Map[row_index][col_index+1] == 1:
            deleteIsland(Map,row_index,col_index+1) 
    #go down
    if len(Map) > row_index+1:
        if Map[row_index+1][col_index] == 1:
            deleteIsland(Map,row_index+1,col_index)
         
    #go up
    if row_index > 0:
        if Map[row_index-1][col_index] == 1:
            deleteIsland(Map,row_index-1,col_index)
    return True

def countIsland(Map):
    count = 0 
    temp_map = Map
    for firstindex,row in enumerate(temp_map):
        for secondindex,col in enumerate(row):
            if col == 1:
                # print(col,"     row: ",firstindex,"     column: ",secondindex)
                deleteIsland(temp_map,firstindex,secondindex)
                count += 1
    return count

Input = input("Enter Input : ").split('/')
Map=[]

for i in Input:
    temp=[*i]
    temp = list(map(int,temp))
    Map.append(temp)  

print(f"Island have : {countIsland(Map)}")