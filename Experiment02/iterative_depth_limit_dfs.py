graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F', 'G'],
    'D' : [],
    'E' : [],
    'F' : [],
    'G' : []
}
start = input("Enter start node    : ")
goal = input("Enter the goal node : ")
level = 0
path = []
maxiteration = 100

def dldfs(start, goal, graph, path, level, maxlim):
    print("Current level : ", level)
    path.append(start)
    if start == goal:
        print("goal found")
        return path
    if level == maxlim:
        print("Maximum Level Reached")
        return False
    print("expanding node: ",start)
    neighbour = graph[start]
    for i in neighbour:
        if dldfs(i, goal, graph, path, level+1, maxlim):
            return path
        path.pop()
    return False

def iterativedldfs(start, goal, graph, maxiteration):
    for i in range(maxiteration):
        path = []
        print("iteration: ", i+1)
        if dldfs(start, goal, graph, path, level, i):
            print("goal found")
            print("path: ", path)
            return True
    return False

iterativedldfs(start, goal, graph, maxiteration)