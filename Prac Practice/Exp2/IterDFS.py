graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F', 'G'],
    'D' : [],
    'E' : [],
    'F' : [],
    'G' : []
}
def depthLtdDFS(graph, start, goal, depth_limit):
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

def itrDFS(graph, start, goal, max_depth_limit):
    for depth_limit in range(1, max_depth_limit+1):
        visited = depthLtdDFS(graph, start, goal, depth_limit)
        print(f"{depth_limit} : {visited}")
        if visited is not None:
            return
        
itrDFS(graph, "A", "F", 3)