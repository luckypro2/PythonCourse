while True:
    z = input(f'Введи коэффициент a: ')
    if not z.isdigit():
        print ('Введи число!')
        z = input(f'Введи коэффициент a: ')
    elif z.isdigit():
        a = int(z)
    s = input(f'Введи коэффициент b: ')
    if not s.isdigit():
        print ('Введи число!')
        s = input(f'Введи коэффициент b: ')
    elif s.isdigit():
        b = int(s)
    h = input(f'Введи коэффициент c: ')
    if not h.isdigit():
        print ('Введи число!')
        h = input(f'Введи коэффициент c: ')
    elif h.isdigit():
        c = int(h)
        break
d = (b**2 - 4*a*c)    
if d >= 0:
    x_1 = (-b + d**(1/2))/(2*a)
    print(x_1) 
    x_2 = (-b - d**(1/2))/(2*a)
    print(x_2)
elif d < 0:
    print ('Уравнение не имеет действительных корней')
    

    
