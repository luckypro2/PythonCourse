import random

x = random.randint(1, 100)

while True:
    a = input (f'Введи число: ')
    a=int(a)
    if x > a:
        print ('Загаданное число больше')
    elif x < a:
        print ('Загаданное число меньше')
    elif x == a:
        print ('Молодцом')
        break
    
