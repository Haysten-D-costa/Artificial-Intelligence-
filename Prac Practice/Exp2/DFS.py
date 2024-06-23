graph = {
    'A' : ['B', 'C'],
    'B' : ['D'],
    'C' : ['E'],
    'D' : ['F'],
    'E' : [],
    'F' : [],
}
start = input("Enter start / root node : ")

def DFS(graph):
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()
        if(node not in visited):
            visited.append(node)
            neighbours = graph[node]

        for neighbour in neighbours:
            stack.append(neighbour)
    return visited

print(f"DFS Traversal : {DFS(graph)}")