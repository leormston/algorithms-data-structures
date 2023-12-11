
def bfs(graph, source, val):
    """breadth first searching an adjacency matrix"""
    seen = []
    prev = []
    for i in range(len(graph)):
        seen.append(False)
        prev.append(-1)
    
    seen[0] = source
    queue = [source]

    while(len(queue) > 0):
        curr = queue.pop(0)
        if(curr == val):
            break
        
        adjacencies = graph[curr]
        for i in range(len(graph)):
            if(adjacencies[i] == 0):
                continue
            if(seen[i]):
                continue

            seen[i]= True
            prev[i] = curr

            queue.append(i)
            
        # seen[curr] = True

    curr = val
    out = []

    while(prev[curr] != -1):
        out.append(curr)
        curr = prev[curr]

    if len(out):
        out.append(source)
        out.reverse()
        return out
    
    return False

    



if __name__ == "__main__":
    ajacency_matrix = [[0, 1, 0, 1],
                       [0, 0, 1, 0],
                       [1, 0, 0, 0],
                       [0, 0, 1, 0]]
    
    print(bfs(ajacency_matrix, 0, 1))