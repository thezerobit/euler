def getdigit(n):
  table = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
  return table[n]

def gettens(n):
  table = {20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty',70:'seventy',80:'eighty',90:'ninety'}
  return table[n]

def getteens(n):
  table = {10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}
  return table[n]

def getstring(num):
  if(num == 1000):
    return 'one thousand'
  elif(num == 0):
    return 'zero'
  result = ''
  if(num > 99):
    hundreds = num / 100
    result += getdigit(hundreds)
    result += ' hundred '
    num = num % 100
    if num > 0:
      result += 'and '
  if num > 19:
    tens = num - (num % 10)
    result += gettens(tens)
    num = num - tens  
    if(num > 0):
      result += '-'
  if(num > 9):
    result += getteens(num)
  elif(num == 0):
    pass
  else:
    result += getdigit(num)
  #print result
  return result

def countletters(s):
  res = s.replace(' ', '')
  res = res.replace('-', '')
  #print res
  return len(res)

sum = 0
for num in xrange(1, 1001):
  sum += countletters(getstring(num))

print sum