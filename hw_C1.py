a = str(input(f'Введи набор чисел: '))
b = a.split()
start = 1
stop = len(b)
step = 1
for i in range(start, stop, step):
    if b[i] > b[i-1]:
        print (b[i])
