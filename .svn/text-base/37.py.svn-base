# Next, please, too easy
from math import sqrt
def isprime(num):
  if num < 0:
    return False
  if num < 10:
    arr = [False, False, True, True, False, True, False, True, False, False]
    return arr[num]
  if (num % 2) == 0:
    return False
  sqrroot = int(sqrt(num))
  for d in range(3,sqrroot+1,2):
    if (num % d) == 0:
      return False
  return True

def truncatableprime(num, verbose = False):
  if not isprime(num):
    if verbose: print num, "is not prime"
    return False
  strnum = str(num)
  for x in range(1,len(strnum)):
    if not isprime(int(strnum[:-x])):
      if verbose: print int(strnum[:-x]), "is not prime"
      return False
    if verbose: print int(strnum[:-x]), "is prime"
  for y in range(1,len(strnum)):
    if not isprime(int(strnum[y:])):
      if verbose: print int(strnum[y:]), "is not prime"
      return False
    if verbose: print int(strnum[y:]), "is prime"
  return True

count = 0
sum = 0
test = 10


while count < 11:
  if truncatableprime(test):
    count += 1
    sum += test
  test += 1

print sum