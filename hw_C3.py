a = str(input(f'Введи фразу: '))
b = a.split()
c = []
for i in b:
    l = len(i)
    c.append(l)
print(min(c))
    
