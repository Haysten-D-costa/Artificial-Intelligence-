import numpy as np

def activation(v):
    if v >= 4.5:
        return 1
    else:
        return 0
    
def perception(x,w,b):
    net = np.dot(x,w) + b
    return activation(net)

def AND3(x):
    w = np.array([1,1,1])
    b = 1.5
    return perception(x,w,b)

test1 = np.array([0,0,0])
test2 = np.array([0,0,1])
test3 = np.array([0,1,0])
test4 = np.array([0,1,1])
test5 = np.array([1,0,0])
test6 = np.array([1,0,1])
test7 = np.array([1,1,0])
test8 = np.array([1,1,1])
print(f"(0,0,0) : {AND3(test1)}")
print(f"(0,0,1) : {AND3(test2)}")
print(f"(0,1,0) : {AND3(test3)}")
print(f"(0,1,1) : {AND3(test4)}")
print(f"(1,0,0) : {AND3(test5)}")
print(f"(1,0,1) : {AND3(test6)}")
print(f"(1,1,0) : {AND3(test7)}")
print(f"(1,1,1) : {AND3(test8)}")
