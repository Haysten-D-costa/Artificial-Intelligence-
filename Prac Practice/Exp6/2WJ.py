A = int(input("Max Cap for A : "))
B = int(input("Max Cap for B : "))
Ai = int(input("Initial Cap for A : "))
Bi = int(input("Initial Cap for A : "))
Af = int(input("Final Cap for A : "))

print("1. Fill A Completely")
print("2. Fill B Completely")
print("3. Empty A")
print("4. Empty B")
print("5. A -> B Until Full")
print("6. B -> A Until Full")
print("7. A -> B Completely")
print("8. B -> A Completely")

while Ai != Af:
    op = int(input("Enter operation : "))
    if(op == 1):
        Ai = A
    elif(op == 2):
        Bi = B
    elif(op == 3):
        Ai = 0
    elif(op == 4):
        Bi = 0
    elif(op == 5):
        if(B-Bi > Ai):
            Bi = Bi + Ai
            Ai = 0
        else:
            Bi = B
            Ai = Ai - (B-Bi)         
    elif(op == 6):
        if(A-Ai > Bi):
            Ai = Ai + Bi
            Bi = 0
        else:
            Bi = Bi - (A-Ai)
            Ai = A
    elif(op == 7):
        Bi = Bi + Ai
        Ai = 0
    elif(op == 8):
        Ai = Ai + Bi
        Bi = 0
    print(f"A{Ai} B{Bi}")