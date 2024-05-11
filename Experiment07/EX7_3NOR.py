import numpy as np
def activation(v):
    if v==0.5:
        return 1
    else:
        return 0

def perceptron(x,w,b):
    r=np.dot(x,w)+b
    return activation(r)
def NOR_gate(x):
    w=np.array([1,1,1])
    b=0.5
    return perceptron(x,w,b)
EX1=np.array([0,0,0])
EX2=np.array([0,0,1])
EX3=np.array([0,1,0])
EX4=np.array([0,1,1])
EX5=np.array([1,0,0])
EX6=np.array([1,0,1])
EX7=np.array([1,1,0])
EX8=np.array([1,1,1])
print("NOR(0,0,0):",NOR_gate(EX1))
print("NOR(0,0,1):",NOR_gate(EX2))
print("NOR(0,1,0):",NOR_gate(EX3))
print("NOR(0,1,1):",NOR_gate(EX4))
print("NOR(1,0,0):",NOR_gate(EX5))
print("NOR(1,0,1):",NOR_gate(EX6))
print("NOR(1,1,0):",NOR_gate(EX7))
print("NOR(1,1,1):",NOR_gate(EX8))

    