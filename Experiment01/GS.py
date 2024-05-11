'''
    Experiment 01 : 
    AIM : To implement Goal Search....
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
goal = input("Enter the goal node  : ")

def goalSearch(graph):
    visited = []
    queue = [start]

    if start == goal:
        print("Start node itself is a goal Node")
        visited.append(start)
        return visited
    else:
        visited.append(start)

        while queue:
            node = queue.pop(0)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
                
                if neighbour == goal:
                    return visited
        return "Connecting path doesnt exist !"

print(f"GS Traversal : {goalSearch(graph)}")
