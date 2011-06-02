import sys
def s(num):
  arr = [x for x in str(num)]
  arr.sort()
  strnum = ''.join(arr)
  return strnum

t = 1
while True:
  b = s(t*2)
  if (b == s(t*3)) and (b == s(t*4)) and (b == s(t*5)) and (b == s(t*6)):
    print t
    sys.exit(0)
  t += 1