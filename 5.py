A=int(input('Enter a Number\n'))
B = 1
while True:       
    if A % B == 0:
        A //= B        
    else:
        break      
    B += 1
if A == 1:
    print('This is a Factorial Number :)')
else:
    print('Try Again,This is Not a Factorial Number!')
