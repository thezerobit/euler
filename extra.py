from math import sqrt

def triangle(num):
  return (num * (num + 1)) / 2

# begin ignore
primes = [2, 3, 5]

def isprime(num):
  sqrroot = int(sqrt(num))
  for d in range(3,sqrroot+1,2):
    if (num % d) == 0:
      return False
  return True

def getnextprime(p):
  p += 1
  while not isprime(p):
    p += 1
  return p

def getprimes(max):
  while primes[-1] < max:
    primes.append(getnexprime(primes[-1]))
  return primes
#end ignore

def countfactors(n):
  factors = 0
  tri = triangle(n)
  for div in range(1, tri+1):
    if (tri % div) == 0:
      factors += 1
  return factors

for n in range(1,502):
  print "triangle(%d) -> %d -> %d"%(n,triangle(n),countfactors(n))
