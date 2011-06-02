# works only because there are no repeating digits, could 
# have done by hand quicker, but there's nothing like
# code to prove you solved it.

def odin(inp, out, func):
  global answer
  if len(inp) == 1:
    test = out + inp
    func(test)
  else:
    for x in xrange(len(inp)):
      odin(inp[:x] + inp[x+1:], out + inp[x], func)

f = open('keylog.txt')
contents = f.read()
lines = contents.splitlines()

digits = []

def getord(line, pk):
  o = []
  for d in line:
    for p in xrange(len(pk)):
      if d == pk[p]:
        o.append(p)
  return o

def check(pk):
  global lines
  for line in lines:
    o = getord(line, pk)
    if (o[0] > o[1]) or (o[1] > o[2]):
      return
  print "success:",pk

for line in lines:
  for digit in line:
    if not digit in digits:
      digits.append(digit)

teststring = ''.join(digits)

odin(teststring,'',check)


  