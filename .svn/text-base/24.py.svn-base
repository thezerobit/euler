import sys

count = 0

def permutate(inp, out):
  global count
  #print 'permutate', inp, out
  if len(inp) == 1:
    count += 1
    if count == 1000000:
      print out + inp
      sys.exit(0)
  else:
    for n in xrange(len(inp)):
      permutate(inp[:n] + inp[n+1:], out + inp[n])

permutate('0123456789', '')