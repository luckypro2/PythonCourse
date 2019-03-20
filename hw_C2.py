a = input (f'Введи число: ')
if not a.isdigit():
    print ('Ты должен был ввести число!!!')
c = []
s = 0
m = 1
for i, symbol in enumerate (a):
    c.append (symbol)
for i in c:
    s += int(i)
    m *= int(i)
print (s)
print (m)
