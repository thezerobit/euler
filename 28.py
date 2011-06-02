suma = 1

width = 1001

last = width * width
skip = 1
skip_inc = 2
hit = 1
currskip = skip
for n in xrange(2, last + 1):
  if currskip > 0:
    currskip -= 1
  else:
    if hit == 1:
      suma += n
      hit += 1
      currskip = skip
    elif hit == 2:
      suma += n
      hit += 1
      currskip = skip
    elif hit == 3:
      suma += n
      hit += 1
      currskip = skip
    elif hit == 4:
      suma += n
      hit = 1
      skip += skip_inc
      currskip = skip

print suma