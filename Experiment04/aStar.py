graph=[['A','H',7,0],
       ['A','B',1,3],
       ['A','C',2,4],
       ['B','D',4,2],
       ['B','E',6,6],
       ['D','E',7,6],
       ['C','F',3,3],
       ['C','G',2,1],
       ['D','H',5,0],
       ['F','H',1,0],
       ['G','H',2,0]
       ]

start=input("Enter the start node : ")
goal=input("Enter the goal node  : ")
temp=[]
temp1=[]
for i in graph:
    temp.append(i[0])
    temp1.append(i[1])
nodes=set(temp).union(set(temp1))

cost=dict()
path=dict()

for i in nodes:
    cost[i]=9999
    path[i]=' '

open=set()
close=set()

open.add(start)
cost[start]=0
path[start]=start

def astar(graph,open,close,cost,current_node):
    if current_node in open:
        open.remove(current_node)
    close.add(current_node)
    for i in graph:
        if(i[0] == current_node and cost[i[0]]+i[2]+i[3] < cost[i[1]]):
            open.add(i[1])
            cost[i[1]]=cost[i[0]]+i[2]+i[3]
            path[i[1]]=path[i[0]]+'->'+i[1]
    cost[current_node]=9999
    small=min(cost,key=cost.get) #min(iterable,key)
    if small not in close:
        astar(graph, open, close, cost, small)

astar(graph,open,close,cost,start)
print("path is ",path[goal])
path1  = path[goal].replace('->','')
list1  = path1[1:-1]

sum = 0
for elements in list1:
    for j in graph:
        if j[1] == elements:
            sum  = sum + j[3]

print(f"Cost = {cost[goal] - sum}")
            