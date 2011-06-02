# Kinda slow, takes ~ a minute
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

answer = 0 

def odin(inp, out):
  global answer
  if len(inp) == 1:
    test = int(out + inp)
    if isprime(test):
      if test > answer:
        answer = test
  else:
    for x in xrange(len(inp)):
      odin(inp[:x] + inp[x+1:], out + inp[x]) 

test = '123'
for x in xrange(4,10):
  test = test + str(x)
  print test
  odin(test,'')

print answer