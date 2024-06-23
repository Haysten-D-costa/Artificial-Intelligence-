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
goal = input("Enter goal node   : ")

def GoalDFS(graph):
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            if node == goal:
                return visited
            neighbours = graph[node]

        for neighbour in neighbours:
            stack.append(neighbour)
    return "- No such goal exists !"

print(f"DFS Goal : {GoalDFS(graph)}")       