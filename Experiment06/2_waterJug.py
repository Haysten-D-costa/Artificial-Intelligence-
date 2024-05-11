jugA = int(input("Enter max capacity of jugA : "))
jugB = int(input("Enter max capacity of jugB : "))
jugAi = int(input("Enter initial water in jugA : "))
jugBi = int(input("Enter initial water in jugB : "))
jugAf = int(input("Enter final capacity of jugA : "))

print("\nOP1 : Fill the jugA completely")
print("OP2 : Fill the jugB completely")
print("OP3 : Empty the jugA on to the ground")
print("OP4 : Empty the jugB on to the ground")
print("OP5 : Pour the water from jugA to jugB until it is full")
print("OP6 : Pour the water from jugB to jugA until it is full")
print("OP7 : Pour entire water from jugA to jugB")
print("OP8 : Pour entire water from jugB to jugA\n")

while(jugAi != jugAf):
    op = int(input("Enter the operation number : "))
    if(op == 1):
        jugAi = jugA
    elif(op == 2):
        jugBi = jugB
    elif(op == 3):
        jugAi = 0
    elif(op == 4):
        jugBi = 0
    elif(op == 5):
        if(jugB-jugBi > jugAi):
            jugBi = jugBi + jugAi
            jugAi = 0
        else:
            jugBi = jugB
            jugAi = jugAi - (jugB-jugBi)
    elif(op == 6):
        if(jugA-jugAi > jugBi):
            jugAi = jugAi + jugBi
            jugBi = 0
        else:
            jugBi = jugBi - (jugA-jugAi)
            jugAi = jugA
    elif(op == 7):
        jugBi = jugBi + jugAi
        jugAi = 0
    elif(op == 8):
        jugAi = jugAi + jugBi
        jugBi = 0
    print(f"Result : jugA-{jugAi} and jugB-{jugBi} ")