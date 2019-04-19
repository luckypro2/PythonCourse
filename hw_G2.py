#Fermat's little theorem states that if p is a prime number, then for any integer a, the number a**p − a is an integer multiple of p.

def primes(end):
    for p in range(2, end):
        if (2**(p)-2)% p == 0:
            yield p

for number in primes(35000):
    print(number, end = ' ')
