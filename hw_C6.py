with open ('rosalind_subs.txt', 'r') as file:
    a = file.read()
a = a.split('\n')

b=a[0]
c=a[1]

for i in range(len(b)):
    if c[0:len(c)] == b[i:len(c)+i]:
        print (i+1, end=' ')
