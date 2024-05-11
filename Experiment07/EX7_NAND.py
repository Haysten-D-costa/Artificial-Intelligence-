import numpy as np
def activation(v):
    if v<=1.5:
        return 1
    else:
        return 0

def perceptron(x,w,b):
    r=np.dot(x,w)+b
    return activation(r)
def NAND_gate(x):
    w=np.array([1,1])
    b=0.5
    return perceptron(x,w,b)
case1=np.array([0,0])
case2=np.array([0,1])
case3=np.array([1,0])
case4=np.array([1,1])
print("NAND(0,0):",NAND_gate(case1))
print("NAND(0,1):",NAND_gate(case2))
print("NAND(1,0):",NAND_gate(case3))
print("NAND(1,1):",NAND_gate(case4))

    