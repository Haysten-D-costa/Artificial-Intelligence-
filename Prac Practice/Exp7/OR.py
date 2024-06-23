import numpy as np

def activation(v):
    if v>=2.5:
        return 1
    else:
        return 0
    
def perception(x,w,b):
    net=np.dot(x,w)+b
    return activation(net)

def OR(x):
    w=np.array([1,1])
    b=1.5
    return perception(x,w,b)

test1 = np.array([0,0])
test2 = np.array([0,1])
test3 = np.array([1,0])
test4 = np.array([1,1])
print(f"(0,0) : {OR(test1)}")
print(f"(0,1) : {OR(test2)}")
print(f"(1,0) : {OR(test3)}")
print(f"(1,1) : {OR(test4)}")