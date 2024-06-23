def depthLtd(graph, start, goal, depth_limit):
    def DFS(current_node, goal, visited, depth):
        if current_node == goal:
            return visited
        if depth >= depth_limit:
            return None
        
        for neighbour in graph[current_node]:
            if neighbour not in visited:
                result = DFS(neighbour, goal, visited+[neighbour], depth+1)
                if result is not None:
                    return result
                
        return None
    return DFS(start, goal, [start], 0)

graph = {
    'A' : ['B', 'C'],
    'B' : ['D'],
    'C' : ['E'],
    'D' : ['F'],
    'E' : [],
    'F' : [],
}
start = "A"
goal = "E"
depth_limit = 1

print(f"-> {depthLtd(graph, start, goal, depth_limit)}")
