a = str(input(f'Введи набор чисел: '))
b = a.split()
for i in range(len(b)):
    if b[i] > b[i-1]:
        print (b[i])
