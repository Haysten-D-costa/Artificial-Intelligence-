'''
    Experiment 01 : Breadth First Search
'''
graph = {
    'A' : ['B', 'C'],
    'B' : ['D'],
    'C' : ['E'],
    'D' : ['F'],
    'E' : ['F'],
    'F' : []
}
start = input("Enter the start node : ")

def breadthFirstSearch(graph):
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

print(f"BFS Traversal : {breadthFirstSearch(graph)}")