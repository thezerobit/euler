# too easy, brute search runs < 1 second with lookup table
# for factorial
def fact(x): return (1 if x==0 else x * fact(x-1))

fct=[]

for x in xrange(101):
  fct.append(fact(x))

def ncr(n,r):
  global fct
  return fct[n] / (fct[r] * (fct[n-r]))

count = 0

for r in xrange(1, 100):
  for n in xrange(r+1, 101):
    if ncr(n,r) > 1000000:
      count += 1

print count