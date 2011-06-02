# the thing(s,p,d) function raises a number to a power, keeping d last digits 

#print str(28433 * (2 ** 7830457) + 1)[-10:]
#just kidding :)

def thing(n, p, d):
  res = 1
  while(p > 100):
    res *= (n ** 100)
    res %= (10 ** d)
    p -= 100
  res *= (n ** p)
  res %= (10 ** d)
  return res

print str(28433 * (thing(2,7830457,10)) + 1)[-10:]
