# a little slow ( 2 or 3 minutes) but is correct
def check(a,b,c):
  return (a*a + b*b) == c*c

def counttris(num):
  count = 0
  for a in xrange(num / 2):
    for b in xrange(num / 2):
      c = num - a - b
      if check(a,b,c):
         count += 1
  return count

maxtris = 0
p = 0

for x in xrange(6, 1001):
  if (x % 50) == 0:
    print x
  ntris = counttris(x)
  if ntris > maxtris:
    maxtris = ntris
    p = x

print p