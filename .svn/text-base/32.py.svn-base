def odin(inp, out, func):
  global answer
  if len(inp) == 1:
    test = out + inp
    func(test)
  else:
    for x in xrange(len(inp)):
      odin(inp[:x] + inp[x+1:], out + inp[x], func) 

pdg = {}

def check(a,b,c):
  global pdg
  if (a * b) == c:
    pdg[c] = c
  
def tester(s):
  check(int(s[:2]),int(s[2:5]),int(s[5:]))
  check(int(s[:1]),int(s[1:5]),int(s[5:]))

odin('123456789','',tester)

sum = 0
for n in pdg:
  sum += n

print pdg

print sum