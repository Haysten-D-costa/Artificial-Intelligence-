graph = {
    'A' : ['B', 'C'],
    'B' : ['D'],
    'C' : ['E'],
    'D' : ['F'],
    'E' : ['F'],
    'F' : [],
}
start = input("Enter start node : ")
goal =  input("Enter goal node  : ")

def GoalBFS(graph):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            if node == goal:
                return visited
            neighbours = graph[node]

        for neighbour in neighbours:
            queue.append(neighbour)
    return "- No such goal found !"

print(f"BFS Goal Traversal : {GoalBFS(graph)}")