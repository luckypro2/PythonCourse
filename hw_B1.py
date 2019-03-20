with open('rosalind_rna.txt', 'r') as file_in:
    text = file_in.read()

text = text.replace("T", "U")

with open ('rosalind_rna2.txt', 'w') as file_out:
    file_out.write(text)

with open ('rosalind_rna2.txt', 'r') as file:
    a = file.read()

print(a)
    
