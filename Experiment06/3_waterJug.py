#3 water jug problem
# max-capacities = (8, 5, 3)
x = int(input("Enter the maximum capacity of jug A: "))
y = int(input("Enter the maximum capacity of jug B: "))
z = int(input("Enter the maximum capacity of jug C: "))
goalX = int(input("Enter the goal capacity in Jug A: "))
goalY = int(input("Enter the goal capacity in Jug B: "))
visited = {}
path = []

def get_all_states(state):
    a = state[0]
    b = state[1]
    c = state[2]

    if a == goalX and b == goalY:
        path.append(state)
        return True

    if (a, b, c) in visited:
        return False

    visited[(a, b, c)] = 1

    if a > 0:
        if (a + b) <= y:
            if get_all_states((0, a + b, c)):
                path.append(state)
                return True
        else:
            if get_all_states((a - (y - b), y, c)):
                path.append(state)
                return True
        if (a + c) <= z:
            if get_all_states((0, b, a + c)):
                path.append(state)
                return True
        else:
            if get_all_states((a - (z - c), b, z)):
                path.append(state)
                return True

    if b > 0:
        if (a + b) <= x:
            if get_all_states((a + b, 0, c)):
                path.append(state)
                return True
        else:
            if get_all_states((x, b - (x - a), c)):
                path.append(state)
                return True
        if (b + c) <= z:
            if get_all_states((a, 0, b + c)):
                path.append(state)
                return True
        else:
            if get_all_states((a, b - (z - c), z)):
                path.append(state)
                return True

    if c > 0:
        if (a + c) <= x:
            if get_all_states((a + c, b, 0)):
                path.append(state)
                return True
        else:
            if get_all_states((x, b, c - (x - a))):
                path.append(state)
                return True
        if (b + c) <= y:
            if get_all_states((a, b + c, 0)):
                path.append(state)
                return True
        else:
            if get_all_states((a, y, c - (y - b))):
                path.append(state)
                return True

    return False

initial_state = (8, 0, 0)
print("Solution : \n")
get_all_states(initial_state)
path.reverse()
for i in path:
    print(i)