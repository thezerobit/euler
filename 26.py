#warning: this code is "lucky", not good or correct
def is_repeating(num):
  for x in xrange(1, 100):
    div = 10 ** x
    if (div % num) == 0:
      return False
  return True

def countdigitsrep(num):
  limit = 1000
  for x in xrange(1, limit):
    div = (10 ** x) - 1
    if (div % num) == 0:
      return x 
  return 0

#for n in xrange(1, 10):
#  print n, is_repeating(n)

longest = 0
inp = 0

for x in xrange(1, 1000):
  if is_repeating(x):
    dr = countdigitsrep(x)
    if dr > longest:
      longest = dr
      inp = x

print inp, longest
