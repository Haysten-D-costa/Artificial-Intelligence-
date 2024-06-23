import numpy as np

def activation(v):
    if v >= 2.5:
        return 0
    else:
        return 1
    
def perception(x,w,b):
    net=np.dot(x,w)+b
    return activation(net)

def NOR(x):
    w=np.array([1,1])
    b=1.5
    return perception(x,w,b)

test1 = np.array([0,0])
test2 = np.array([0,1])
test3 = np.array([1,0])
test4 = np.array([1,1])
print(f"(0,0) : {NOR(test1)}")
print(f"(0,1) : {NOR(test2)}")
print(f"(1,0) : {NOR(test3)}")
print(f"(1,1) : {NOR(test4)}")