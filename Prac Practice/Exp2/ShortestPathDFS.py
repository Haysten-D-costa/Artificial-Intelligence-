graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F', 'G'],
    'D' : [],
    'E' : [],
    'F' : [],
    'G' : []
}
start = input("Enter start node : ")
goal = input("Enter goal node : ")

def ShortestPathDFS(graph):
    visited = []
    stack = [start]
    
    while stack:
        path = stack.pop()
        node = path[-1]
        if node not in visited:
            visited.append(node)
            neighbours = graph[node]

        for neighbour in neighbours:
            new_path = list(path)
            new_path.append(neighbour)
            stack.append(new_path)

            if neighbour == goal:
                return new_path



print(f"Shortest DFS Path is : {ShortestPathDFS(graph)}")
