from math import sqrt

max = 1000000

def isprime(num):
  if num < 0:
    return False
  if num < 10:
    arr = [False, False, True, True, False, True, False, True, False, False]
    return arr[num]
  if (num % 10000) == 0:
    print num
  if (num % 2) == 0:
    return False
  sqrroot = int(sqrt(num))
  for d in range(3,sqrroot+1,2):
    if (num % d) == 0:
      return False
  return True

primes = [isprime(x) for x in xrange(max)]

def iscircularprime(num):
  global primes
  strnum = str(num)
  for x in xrange(len(strnum)):
    test = strnum[x:] + strnum[:x]
    if not primes[int(test)]:
      return False
  return True

print 'done calculating primes under ' + str(max)

count = 0

for n in xrange(max):
  if iscircularprime(n):
    count += 1

print count


