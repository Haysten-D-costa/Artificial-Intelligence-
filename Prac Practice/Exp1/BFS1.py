graph = {
    'A' : ['B', 'C'],
    'B' : ['D'],
    'C' : ['E'],
    'D' : ['F'],
    'E' : [],
    'F' : [],
}
start = "A"

def BFS(graph):
    visited = []
    queue = [start]
    
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            neighbours = graph[node]
        
        for neighbour in neighbours:
            queue.append(neighbour)
    return visited

print(f"-> {BFS(graph)}")