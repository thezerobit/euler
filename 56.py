# too easy with Python
def sumdp(a,b):
  pw = a ** b
  sum = 0
  for digit in str(pw):
    sum += int(digit)
  return sum

maxsum = 0
maxa = 0
maxb = 0

for a in xrange(1,100):
  for b in xrange(1,100):
    sdp = sumdp(a,b)
    if sdp > maxsum:
      maxsum = sdp
      maxa = a
      maxb = b

print a,b,maxsum