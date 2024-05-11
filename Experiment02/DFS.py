'''
    Experiment 02 : Depth First Search
'''
graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F', 'G'],
    'D' : [],
    'E' : [],
    'F' : [],
    'G' : []
}
start = input("Enter the start node : ")

def depthFirstSearch(graph):
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()
        
        if node not in visited:
            visited.append(node)
            neighbours = graph[node]

            for neighbour in neighbours:
                stack.append(neighbour)
    return visited     

print(f"DFS Traversal : {depthFirstSearch(graph)}")