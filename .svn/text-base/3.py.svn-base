value = 600851475143

running = value

pfactors = []

ptest = 2

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

while running > 1:
    if (running % ptest) == 0:
        pfactors.append(ptest)
        running = running / ptest
    else:
        ptest = get_next_prime(ptest)

print ptest
