with open ('rosalind_hamm.txt', 'r') as file:
    a = file.read()

a = a.split('\n')
count_ham = 0
b = a[0]
c = a[1]

for i, symbol in enumerate(b):
    if c[i] != b[i]:
        count_ham += 1

print(count_ham)
