def has_unvisisited(seen, dists):
    """checks if node is unvisisited and distance of i is less than infinity"""
    for i in range(len(seen)):
        if seen[i] is False and dists[i] < float('inf'):
            return True
    return False


def get_lowest_unvisisted(seen, dists):
    """finds the lowest index reachable that has not been seen yet"""
    index = -1
    lowest_distance = float('inf')

    for i in range(len(seen)):
        if(seen[i]):
            continue
        if (lowest_distance > dists[i]):
            lowest_distance = dists[i]
            index = i

    return index

def dijkstra_list(source, sink, adj_list):
    """
    source: starting node
    sink: the target node we are looking for 
    adj_list: adjacency list containing mapping details of all the nodes
    """

    seen = []
    dists = []
    prev = []
    for i in range(len(adj_list)):
        seen.append(False)
        dists.append(float('inf'))
        prev.append(float(-1))


    dists[source] = 0

    while (get_lowest_unvisisted(seen, dists)):
        curr = get_lowest_unvisisted(seen, dists)
        seen[curr] = True

        adjs = adj_list[curr]
        for i in range(len(adjs)):
            edge = adjs[i]
            if seen[edge.to]:
                continue
            dist = dists[curr] + edge.weight
            if dist< dists[edge.to]:
                dists[edge.to] = dist
                prev[edge.to] = curr

    out = []
    curr = sink

    while(prev[curr] != -1):
        out.append(curr)
        curr = prev[curr]
    
    out.append(source)
    out.reverse()
    return out
if __name__ == "__main__":
    pass