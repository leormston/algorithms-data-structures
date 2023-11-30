#This represents up, down left and right. Saves us having to enter co-ords when walking
directions = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1]
]


#maze is the maze string 2d array
#wall - define what character represents a wall
#curr is the current co-ords
#end is if we are at the end
#seen is a 2d array originally populated with falses but as we traverse gets populated with truthes
#path is the path we are currently on
def walk(maze, wall, curr, end, seen, path):

    #Base cases
    #1. Off the map
    if(curr['x'] < 0 or curr['x'] >= len(maze[0]) 
       or curr['y'] < 0 or curr['y'] >= len(maze)):
        return False

    #2. On a wall
    if(maze[curr['y']][curr['x']] == wall):
        return False
    
    #4. At the end
    if(curr['x'] == end['x'] and curr['y'] == end['y']):
        path.append(end)
        return True
    
    #3. Already seen this block
    if(seen[curr['y']][curr['x']]):
        return False
    
    seen[curr['y']][curr['x']] = True
    
    path.append(curr)
    
    #recursive step
    for direction in directions:
        x, y =  direction[1], direction[0]
        if walk(maze, 
             wall, 
             {'x': curr['x'] + x, 'y': curr['y'] + y},
             end, seen, path):
            return True

if __name__ == "__main__":
    print("Traversal Starting")
    maze = [
        ["#","#","#", "#", " ", "#", "#"],
        ["#"," "," ", " ", " ", "#", "#"],
        ["#"," ","#", "#", "#", "#", "#"]
    ]
    seen = [[False for x in range(len(maze[0]))] for y in range(len(maze))]
    path = []

    walk(maze, '#', {'x': 4, 'y': 0 }, {'x': 1, 'y': 2}, seen, path)
    print(path)