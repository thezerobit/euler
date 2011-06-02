from math import sqrt

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

ab = 0
greatestcount = 0

for a in xrange(-999,1000):
  for b in xrange(-999,1000):
    n = 0
    while isprime( n * n + n * a + b):
      n += 1
    if n > greatestcount:
      greatestcount = n
      ab = a * b
      print n, a, b

print ab 