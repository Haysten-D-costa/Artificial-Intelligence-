import numpy as np
def activation(v):
    if v<=0.5:
        return 0
    else:
        return 1

def perceptron(x,w,b):
    r=np.dot(x,w)+b
    return activation(r)
def OR_gate(x):
    w=np.array([1,1])
    b=0.5
    return perceptron(x,w,b)
case1=np.array([0,0])
case2=np.array([0,1])
case3=np.array([1,0])
case4=np.array([1,1])
print("OR(0,0):",OR_gate(case1))
print("OR(0,1):",OR_gate(case2))
print("OR(1,0):",OR_gate(case3))
print("OR(1,1):",OR_gate(case4))