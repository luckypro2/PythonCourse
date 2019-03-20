with open('rosalind_revc.txt', 'r') as file_in:
    a = file_in.read()

a = a[::-1]

with open('rosalind_revc2.txt', 'w') as file_out:
    file_out.write(a)

with open('rosalind_revc2.txt', 'r') as file_in:
    b = file_in.read()

c = b.lower()

d = c.replace('a', 'T')
e = d.replace('c', 'G')
f = e.replace('g', 'C')
g = f.replace('t', 'A')
print (g)


        
        
    


