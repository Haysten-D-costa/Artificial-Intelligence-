import numpy as np
def activation(v):
    if v<=0.5:
        return 1
    else:
        return 0

def perceptron(x,w,b):
    r=np.dot(x,w)+b
    return activation(r)
def NOR_gate(x):
    w=np.array([1,1])
    b=0.5
    return perceptron(x,w,b)
case1=np.array([0,0])
case2=np.array([0,1])
case3=np.array([1,0])
case4=np.array([1,1])
print("NOR(0,0):",NOR_gate(np.array([0,0])))
print("NOR(0,1):",NOR_gate(np.array([0,1])))
print("NOR(1,0):",NOR_gate(np.array([1,0])))
print("NOR(1,1):",NOR_gate(np.array([1,1])))

    