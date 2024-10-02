def hill(graph, start, goal):
    visited = []
    open = [([start], 0)]
    
    while open:
        print(open)
        path, cost = open.pop(0)
        node = path[-1]
        if node == goal: return path
        if node not in visited: 
            visited.append(node)
            for neighbour, neighbour_cost in graph[node]:
                new_path = path + [neighbour]
                new_cost = cost + neighbour_cost
                open.append((new_path, new_cost))
            if(len(open) > 1): 
                open = [min(open, key=lambda x:x[1] + heuristic[x[0][-1]])]
    return None

start = "A"
goal = "H"
graph ={
    'A' : [('B', 6), ('C', 9)],
    'B' : [('D', 8), ('E', 7)],
    'C' : [('F', 6), ('G', 2)],
    'D' : [],
    'E' : [('H', 0)],
    'F' : [('H', 0)],
    'G' : [('H', 0)]
}
heuristic = {
    'A' : 7,
    'B' : 3,
    'C' : 7,
    'D' : 1,
    'E' : 2,
    'F' : 8,
    'G' : 4,
    'H' : 0,
}