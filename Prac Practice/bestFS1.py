graph = {
    'A' : [('B', 12), ('C', 4)],
    'B' : [('D', 8), ('E', 7)],
    'C' : [('F', 6), ('G', 2)],
    'D' : [],
    'E' : [('H', 0)],
    'F' : [('H', 0)],
    'G' : [('H', 0)]
}
start = "A"
goal = "H"
open = []
close = []

def bestFS(graph, start, goal, open, close):
    if start not in close:
        print(start)
        close.append(start)
        neighbours = graph[start]

        for i in neighbours:
            if i[0] not in open:
                open.append(i)
                open.sort(key=lambda i:i[1])

    if i[0][0] == goal:
        close.append(i[0][0])
        print(i[0][0])
    else:
        node = open[0]
        open.remove(node)
        bestFS(graph, node[0], goal, open, close)
    return close

print(bestFS(graph, start, goal, open, close))