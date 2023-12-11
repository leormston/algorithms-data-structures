def walk(graph, curr, needle, seen, path):
    if(seen[curr]):
        return False
    
    seen[curr] = True

    #recurse
    #pre
    path.append(curr)

    if(curr == needle):
        return True
    #recurse
    list = graph[curr]
    for i in range(len(list)):
        edge = list[i]
        if (walk(graph, edge.to, needle, seen, path)):
            return True
    
    #post
    path.pop(0)

def dfs(graph, source, val):
    seen  = []
    path = []
    for i in range(len(graph)):
        seen.append(False)
    return walk(graph, source, val, seen, path)


if __name__ == "__main__":
    print(dfs())