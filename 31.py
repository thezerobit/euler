#This program is good.

currency = [200,100,50,20,10,5,2,1]

target = 200

count = 0

def makemoney(target, sofar, index, maxi):
  #print 'makemoney(%d,%d,%d,%d)'%(target, sofar, index, maxi)
  global count, currency
  if sofar < target:
    if (sofar + currency[index]) == target:
      count += 1
      if index < maxi:
        makemoney(target, sofar, index + 1, maxi)
    elif (sofar + currency[index]) > target:
      if index < maxi:
        makemoney(target, sofar, index + 1, maxi)
    elif (sofar + currency[index]) < target:
      if index < maxi:
        makemoney(target, sofar, index + 1, maxi)
      makemoney(target, sofar + currency[index], index, maxi)
  

makemoney(target, 0, 0, 7)

print count