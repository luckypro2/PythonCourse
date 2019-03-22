#n-число месяцев, k-число пар
#F(n)=F(n-1)+ k*F(n-2)
#F(1)=F(2)=1
n=36
k=2
a = [1,1]
for i in range(n-2):
    a.append(0)
for i in a:
    for i in range(n-2):
        a[i+2]=a[i+1]+(k*a[i])

print(a[n-1])


        
