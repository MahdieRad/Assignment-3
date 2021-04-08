import random

Score = 10
Tchars = []
Word = ['Dog', 'IOS', 'Book', 'Happy',
         'Moon', 'Apple', 'Letter', 'Water', 'Flower']
word = random.choice(Word)
while True:
    StrTp = ''

    for i in range(len(Word)):
        if Word[i].lower() in Tchars:
            print(Word[i], end='')
            StrTp += Word[i]
        else:
            print('-', end='')
    if Word == StrTp:
        print('\n You succeeded')
        break
    char = input('\nPlease Enter a Charctr: ')

    if char.lower() in word.lower():
        Tchars.append(char)
    else:
        Score -= 1
    print(Score)

    if Score == 0:
        print("Game Over!")
        break
