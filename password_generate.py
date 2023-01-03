# Password generate dasturi 
from random import shuffle
from string import ascii_letters,digits,punctuation
res = []
letter = int(input("Nechta harf bolishini istaysiz janob: ") )   
number = int(input("Nechta raqam bo'lishini istaysiz janob: "))
symbol = int(input("Nechta belgilar bolishini istaysiz janob: "))
x = list(ascii_letters)
y = list(str(digits))
z = list(punctuation)
shuffle(x)
shuffle(y)
shuffle(z)
while letter > 0:
    res.append(x[letter])                                                           
    letter = letter - 1

while number > 0:
    res.append(y[number])
    number = number - 1

while symbol > 0:
    res.append(z[symbol])                                                          
    symbol = symbol - 1

if len(res) > 8 or len(res) < 8:
    print("Iltimos barcha malumotlarni togri bering parol uzunligi oshib ketdi yoki yetmay qoldi parolning uzunligi 8ta bolishi kerak!")
else: 
    shuffle(res)   
    string =  "".join(res)
    print(string)


