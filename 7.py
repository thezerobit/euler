ptest = 1 
nprime = 10001 

def isprime(num):
    for d in range(2,num):
        if (num % d) == 0:
            return False
    return True

def get_next_prime(num):
    while True:
        num += 1
        if isprime(num):
            return num

for i in range(nprime):
    ptest = get_next_prime(ptest)
    print "%d = %d"%(i + 1, ptest)


print ptest
