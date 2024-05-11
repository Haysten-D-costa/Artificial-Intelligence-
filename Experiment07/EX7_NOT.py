import numpy as np
def activation(v):
    if v<=0.5:
        return 1
    else:
        return 0

def perceptron(x,w,b):
    r=np.dot(x,w)+b
    return activation(r)
def NOT_gate(x):
    w=1
    b=0.5
    return perceptron(x,w,b)

print("NOT(1):",NOT_gate(1))
print("NOT(0):",NOT_gate(0))
    