from math import sqrt

def isprime(num):
    sqrroot = int(sqrt(num))
    for d in range(3,sqrroot+1,2):
        if (num % d) == 0:
            return False
    return True

sum = 5
max = 2000000

print "calculating sum of primes less than %d"%(max)

for n in range(5,max,2):
    if isprime(n):
        #print "%d is prime"%(n)
        sum += n

print sum

