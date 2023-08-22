def deleteIsland(Map,y,x):
    map_row_index = y
    map_col_index = x
    #set current as 0
    Map[map_row_index][map_col_index] = 0
    # if can go left
    if map_col_index > 0:
        if Map[map_row_index][map_col_index - 1] == 1:
            deleteIsland(Map, map_row_index, map_col_index - 1)
    # if can go right
    if len(Map[map_row_index]) > map_col_index + 1:
        if Map[map_row_index][map_col_index + 1] == 1:
            deleteIsland(Map, map_row_index, map_col_index + 1)
    # if can go down
    if len(Map) > map_row_index + 1:
        if Map[map_row_index + 1][map_col_index] == 1:
            deleteIsland(Map, map_row_index + 1, map_col_index)
    # if can go up
    if map_row_index > 0:
        if Map[map_row_index - 1][map_col_index] == 1:
            deleteIsland(Map, map_row_index - 1, map_col_index)
    return True

def countIsland(Map):
    temp_map = Map
    map_count = 0
    for map_row_index, map_row in enumerate(temp_map):
        for map_col_index, map_col in enumerate(map_row):
            # print(map_row_index, map_col_index, map_col)
            if map_col == 1:
                deleteIsland(temp_map, map_row_index, map_col_index)
                map_count += 1
    return map_count

Input = input("Enter Input : ").split('/')

Map=[]

for i in Input:

    temp=[*i]

    temp = list(map(int,temp))

    Map.append(temp)

print(f"Island have : {countIsland(Map)}")