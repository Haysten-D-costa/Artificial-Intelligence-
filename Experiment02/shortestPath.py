'''
    Experiment 02 : Depth First Search Shortest Path
'''
graph = {
    'A' : ['B', 'C'],
    'B' : ['H', 'D', 'E'],
    'C' : ['F', 'G'],
    'D' : [],
    'E' : [],
    'F' : [],
    'G' : ['H', 'I'],
    'H' : [],
    'I' : []
}

start = input("Enter start node : ")
goal = input("Enter goal node  : ")

def dfsShortestPath(graph):
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
                
print(f"Shortest DFS Path is : {dfsShortestPath(graph)}")
