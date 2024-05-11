graph = {
    'A': ['B', 'C'], 
    'B': ['D', 'E'], 
    'C': ['F', 'G'], 
    'D': [], 
    'E': [], 
    'F': [], 
    'G': []
}
start = input("Enter start node    : ")
goal = input("Enter the goal node : ")
maxlim = int(input("Enter the max limit : "))
level = 0
path = []

def depth_limit_dfs(start, goal, graph, path, level, maxlim):
    print("Current level : ", level)
    path.append(start)
    if start == goal:
        print("goal found")
        return path
    if level == maxlim:
        print("Maximum Level Reached")
        return False
    print("Expanding node: ",start)
    neighbours = graph[start]
    for neighbour in neighbours:
        if depth_limit_dfs(neighbour, goal, graph, path, level+1, maxlim):
            return path
        path.pop()
    return False

if depth_limit_dfs(start, goal, graph, path, level, maxlim):
    print("Goal id found")
    print(f"The shortest path is {path}")
else:
    print("Goal not found")
