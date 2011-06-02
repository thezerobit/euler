def tri(n): return (n * (n + 1)) / 2
def pen(n): return (n * (3 * n - 1)) / 2
def hxa(n): return n * (2 * n - 1)

limit = 100000

pens = {}
hxas = {}

for x in xrange(1, limit):
  pens[pen(x)] = x
  hxas[hxa(x)] = x

for y in xrange(286, limit):
  t = tri(y)
  if (t in pens) and (t in hxas):
    print t
