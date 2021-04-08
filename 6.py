Numb = int(input("Enter a Number: "))
A = len(str(Numb))

sum = 0

Temp = Numb
while Temp > 0:
   B = Temp % 10
   sum += B ** A
   Temp //= 10

if Numb == sum:
   print(Numb," Armstrong number")
else:
   print(Numb,"not an Armstrong number")
