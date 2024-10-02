graph = {
    "A": [("B", 1), ("C", 2), ("H", 7)],
    "B": [("D", 4), ("E", 6)],
    "C": [("F", 3), ("G", 2)],
    "D": [("E", 7), ("H", 5)],
    "E": [],
    "F": [("H", 1)],
    "G": [("H", 2)],
    "H": []    
}
heuristic = {
    "A": 0,
    "B": 3,
    "C": 4,
    "D": 2,
    "E": 6,
    "F": 3,
    "G": 1,
    "H": 0
}
def aStar(graph, start, goal):
    visited = []
    open = [([start], 0)]

    while open:
        print(open[0])
        path, cost = open.pop(0)
        node = path[-1]
        if node == goal: return path
        if node not in visited:
            visited.append(node)
            for neighbour, neighbour_cost in graph[node]:
                new_path = path + [neighbour]
                new_cost = cost + neighbour_cost
                open.append((new_path, new_cost))
        open.sort(key=lambda x:x[1] + heuristic[x[0][-1]])
    
start = "A"
goal = "H"
aStar(graph, start, goal)