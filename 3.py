import random

Number1=[]
Rnumber=[]
while len(Rnumber)<21:
    Number1=random.randint(0,2000)
    if Number1 not in Rnumber:
        Rnumber.append(Number1)
print(Rnumber)
