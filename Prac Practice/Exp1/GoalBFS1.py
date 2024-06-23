graph = {
    'A' : ['B', 'C'],
    'B' : ['D'],
    'C' : ['E'],
    'D' : ['F'],
    'E' : [],
    'F' : [],
}
start = "A"
goal = "H"
def GoalBFS(graph):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbours = graph[node]
            
            if node == goal:
                return visited

        for neighbour in neighbours:
            queue.append(neighbour)
    return "-"

print(f" -> {GoalBFS(graph)}")

        