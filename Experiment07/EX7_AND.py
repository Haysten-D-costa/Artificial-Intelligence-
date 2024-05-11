import numpy as np

def activation(v):
    if v<=1.5:
        return 0
    else:
        return 1

def perceptron(x,w,b):
    r=np.dot(x,w)+b
    return activation(r)

def AND_gate(x):
    w=np.array([1,1])
    b=0.5
    return perceptron(x,w,b)

case1=np.array([0,0])
case2=np.array([0,1])
case3=np.array([1,0])
case4=np.array([1,1])
print("AND(0,0):",AND_gate(case1))
print("AND(0,1):",AND_gate(case2))
print("AND(1,0):",AND_gate(case3))
print("AND(1,1):",AND_gate(case4))

    