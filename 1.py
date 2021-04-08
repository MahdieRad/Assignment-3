import random

cScore=0
uScore=0  

items_1=("Rock","Paper","Scissor")
items_2=("Rock","Paper","Scissor","Exit")

while True:
    cScore=random.choice(items_1)

    print("0-Rock")
    print("1-Paper")
    print("2-Scissor")
    print("3-Exit")

    uChoiceIndex=int(input())
    uChoice=items_2[uChoiceIndex]

    print(cScore)

    if cScore=="Rock" and uChoice=="Scissor":
        print("Computer wins")
        cScore+=1
    elif cScore=="Rock" and uChoice=="Paper":
        print("User wins")
        uScore+=1
    elif cScore=="Rock" and uChoice=="Rock":
        print("again!")

    elif cScore=="Scissor" and uChoice=="Paper":
        print("Computer wins")
        cScore+=1
    elif cScore=="Scissor" and uChoice=="Rock":
        print("User wins")
        uScore+=1
    elif cScore=="Scissor" and uChoice=="Scissor":
        print("again!")

    elif cScore=="Paper" and uChoice=="Rock":
        print("Computer wins")
        cScore+=1
    elif cScore=="Paper" and uChoice=="Scissor":
        print("User wins")
        uScore+=1
    elif cScore=="Paper" and uChoice=="Paper":
        print("again!")
    else: 
        print("user_score:",uScore)
        print("computer_score:",cScore)
        break
