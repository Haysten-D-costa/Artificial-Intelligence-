import numpy as np
def activation(v):
    if v==3.5:
        return 0
    else:
        return 1

def perceptron(x,w,b):
    r=np.dot(x,w)+b
    return activation(r)
def NAND_gate(x):
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
print("NAND(0,0,0):",NAND_gate(EX1))
print("NAND(0,0,1):",NAND_gate(EX2))
print("NAND(0,1,0):",NAND_gate(EX3))
print("NAND(0,1,1):",NAND_gate(EX4))
print("NAND(1,0,0):",NAND_gate(EX5))
print("NAND(1,0,1):",NAND_gate(EX6))
print("NAND(1,1,0):",NAND_gate(EX7))
print("NAND(1,1,1):",NAND_gate(EX8))

    