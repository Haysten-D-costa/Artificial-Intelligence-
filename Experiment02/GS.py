'''
    Experiment 02 : Depth First Search considering goal node....
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
visited = []
start = input("Enter the start node : ")
goal = input("Enter the goal node  : ")

def goalDepthFirstSearch(graph, start):
    if start not in visited:
        visited.append(start)
        neighbours = graph[start]
        
        for neighbour in neighbours:
            if goal in visited:
                print(visited)
                break
            else:
                goalDepthFirstSearch(graph, neighbour)

print("\nDFS Traversal to goal node : ")
goalDepthFirstSearch(graph, start)