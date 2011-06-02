#My 50th correct answer, takes ~ 1 second
def is_palindromic(teststr):
  length = len(teststr)
  ntests = length / 2
  for i in range(ntests):
    if teststr[i] != teststr[length - i - 1]:
      return False
  return True

def is_lychrel(num, checks = 0):
  if checks >= 50:
    return True
  s = num + int(str(num)[::-1])
  if is_palindromic(str(s)):
    return False
  else:
    return is_lychrel(s, checks + 1)

count = 0

for n in xrange(1, 10000):
  if is_lychrel(n):
    count += 1

print count


